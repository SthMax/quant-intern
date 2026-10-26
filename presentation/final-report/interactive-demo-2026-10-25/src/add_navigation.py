"""Add native intra-deck navigation to named shapes in an authored PPTX."""

import argparse
import json
from pathlib import Path
import re
from zipfile import ZipFile

from lxml import etree as ET


P = "http://schemas.openxmlformats.org/presentationml/2006/main"
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG = "http://schemas.openxmlformats.org/package/2006/relationships"
NS = {"p": P, "a": A, "r": R, "rel": PKG}
NAV_NAME = re.compile(r"^(?:!!)?nav\.(front|middle|back|home|prev|next)(?:[.\-_].*)?$")


def add_navigation(source: Path, target: Path, report: Path):
    if source.resolve() == target.resolve():
        raise ValueError("Use a separate output path to preserve the base presentation")
    with ZipFile(source) as archive:
        entries = archive.infolist()
        content = {entry.filename: archive.read(entry.filename) for entry in entries}

    slide_paths = sorted(
        [name for name in content if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)],
        key=lambda name: int(re.search(r"slide(\d+)", name).group(1)),
    )
    if len(slide_paths) != 9:
        raise ValueError(f"Expected the nine-state demonstration, found {len(slide_paths)} slides")

    audit = []
    for page, slide_path in enumerate(slide_paths, 1):
        slide = ET.fromstring(content[slide_path])
        rel_path = slide_path.replace("/slides/", "/slides/_rels/") + ".rels"
        relationships = ET.fromstring(content[rel_path])
        targets = {"front": 2, "middle": 4, "back": 7, "home": 1,
                   "prev": max(1, page - 1), "next": page + 1 if page < 9 else 1}
        links = []
        for props in slide.xpath(".//p:cNvPr", namespaces=NS):
            shape_name = props.get("name", "")
            match = NAV_NAME.fullmatch(shape_name)
            if not match:
                continue
            role = match.group(1)
            destination = targets[role]
            rel_id = f"rIdNavSlide{destination}"
            rel = relationships.find(f"{{{PKG}}}Relationship[@Id='{rel_id}']")
            if rel is None:
                rel = ET.SubElement(relationships, f"{{{PKG}}}Relationship")
                rel.set("Id", rel_id)
            rel.set("Type", R + "/slide")
            rel.set("Target", f"slide{destination}.xml")
            rel.attrib.pop("TargetMode", None)
            for old in props.findall(f"{{{A}}}hlinkClick"):
                props.remove(old)
            action = ET.Element(f"{{{A}}}hlinkClick")
            action.set(f"{{{R}}}id", rel_id)
            action.set("action", "ppaction://hlinksldjump")
            action.set("tooltip", {"front": "前台 客户材料", "middle": "中台 材料审核",
                                   "back": "后台 版本更新", "home": "公司全景",
                                   "prev": "上一步", "next": "下一步"}[role])
            props.insert(0, action)
            links.append({"shape": shape_name, "role": role, "target_page": destination})
        found_roles = {item["role"] for item in links}
        if found_roles != set(targets):
            raise ValueError(f"Slide {page} navigation roles missing: {set(targets) - found_roles}")
        content[slide_path] = ET.tostring(slide, xml_declaration=True, encoding="UTF-8", standalone=True)
        content[rel_path] = ET.tostring(relationships, xml_declaration=True, encoding="UTF-8", standalone=True)
        audit.append({"page": page, "links": links})

    target.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(target, "w") as archive:
        for entry in entries:
            archive.writestr(entry, content[entry.filename])
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps({"slides": 9, "navigation": audit}, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"output": str(target.resolve()), "slides": 9,
                      "linked_shapes": sum(len(row["links"]) for row in audit)}, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("target", type=Path)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    add_navigation(args.source, args.target, args.report)
