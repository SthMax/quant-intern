"""Add Morph transitions and a three-part annotation reveal to the demo."""

import argparse
import json
from pathlib import Path
import re
from zipfile import ZipFile

from lxml import etree as ET

P = "http://schemas.openxmlformats.org/presentationml/2006/main"
MC = "http://schemas.openxmlformats.org/markup-compatibility/2006"
P14 = "http://schemas.microsoft.com/office/powerpoint/2010/main"
MORPH = "http://schemas.microsoft.com/office/powerpoint/2015/09/main"
NS = {"p": P, "mc": MC}


def ptag(name):
    return f"{{{P}}}{name}"


def child(parent, name, **attrs):
    return ET.SubElement(parent, ptag(name), {key: str(value) for key, value in attrs.items()})


def start_condition(node, delay):
    child(child(node, "stCondLst"), "cond", delay=delay)


def append_before_extensions(slide, element):
    ext = slide.find(ptag("extLst"))
    slide.insert(slide.index(ext) if ext is not None else len(slide), element)


def add_morph(slide):
    for old in slide.xpath("./p:transition | ./mc:AlternateContent[p:transition or mc:Choice/p:transition]", namespaces=NS):
        slide.remove(old)
    alternate = ET.Element(f"{{{MC}}}AlternateContent", nsmap={"mc": MC})
    choice = ET.SubElement(alternate, f"{{{MC}}}Choice", Requires="p159", nsmap={"p159": MORPH})
    transition = ET.SubElement(choice, ptag("transition"), spd="med", advClick="1", nsmap={"p14": P14})
    transition.set(f"{{{P14}}}dur", "700")
    ET.SubElement(transition, f"{{{MORPH}}}morph", option="byObject")
    fallback = ET.SubElement(alternate, f"{{{MC}}}Fallback")
    child(child(fallback, "transition", spd="fast", advClick="1"), "fade")
    timing = slide.find(ptag("timing"))
    if timing is not None:
        slide.insert(slide.index(timing), alternate)
    else:
        append_before_extensions(slide, alternate)


def add_reveal(slide, groups):
    for old in slide.findall(ptag("timing")):
        slide.remove(old)
    ids = {int(x.get("id")) for x in slide.xpath(".//p:cNvPr", namespaces=NS)}
    timing = ET.Element(ptag("timing"))
    tn_list = child(timing, "tnLst")
    root = child(child(tn_list, "par"), "cTn", id="1", dur="indefinite", restart="never", nodeType="tmRoot")
    root_children = child(root, "childTnLst")
    sequence = child(root_children, "seq", concurrent="1", nextAc="seek")
    main = child(sequence, "cTn", id="2", dur="indefinite", nodeType="mainSeq")
    effects = child(main, "childTnLst")
    group_node = child(child(effects, "par"), "cTn", id="3", fill="hold")
    start_condition(group_node, "0")
    parallel_effects = child(group_node, "childTnLst")
    timer_id = 4
    animated = []
    for index, group in enumerate(groups):
        for item in group["objects"]:
            shape_id = int(item["id"])
            if shape_id not in ids:
                raise ValueError(f"Animation references missing shape {shape_id}")
            node = child(child(parallel_effects, "par"), "cTn", id=timer_id,
                         presetID="1", presetClass="entr", presetSubtype="0",
                         fill="hold", nodeType="withEffect", grpId="0")
            timer_id += 1
            start_condition(node, 150 + index * 550)
            behavior = child(child(child(node, "childTnLst"), "set"), "cBhvr")
            behavior_node = child(behavior, "cTn", id=timer_id, dur="1", fill="hold")
            timer_id += 1
            start_condition(behavior_node, "0")
            child(child(behavior, "tgtEl"), "spTgt", spid=shape_id)
            child(child(behavior, "attrNameLst"), "attrName").text = "style.visibility"
            child(child(behavior.getparent(), "to"), "strVal", val="visible")
            animated.append(shape_id)
    for list_name, event in [("prevCondLst", "onPrev"), ("nextCondLst", "onNext")]:
        condition = child(child(sequence, list_name), "cond", evt=event, delay="0")
        child(child(condition, "tgtEl"), "sldTgt")
    builds = child(timing, "bldLst")
    for shape_id in animated:
        child(builds, "bldP", spid=shape_id, grpId="0", animBg="1")
    append_before_extensions(slide, timing)
    return animated


def main(source, target, hints_path, report_path):
    if source.resolve() == target.resolve():
        raise ValueError("Keep the input presentation unchanged")
    hints = json.loads(hints_path.read_text())
    with ZipFile(source) as archive:
        entries = archive.infolist()
        content = {entry.filename: archive.read(entry.filename) for entry in entries}
    audit = []
    for filename in sorted(content):
        match = re.fullmatch(r"ppt/slides/slide(\d+)\.xml", filename)
        if not match:
            continue
        page = int(match.group(1))
        slide = ET.fromstring(content[filename])
        for props in slide.xpath(".//p:cNvPr", namespaces=NS):
            if props.get("name", "").startswith("nav."):
                props.set("name", "!!" + props.get("name"))
        names = [x.get("name") for x in slide.xpath(".//p:cNvPr", namespaces=NS) if x.get("name", "").startswith("!!")]
        if len(names) != len(set(names)):
            raise ValueError(f"Duplicate Morph names on page {page}")
        add_morph(slide)
        revealed = add_reveal(slide, hints["groups"]) if page == hints["slide"] else []
        content[filename] = ET.tostring(slide, xml_declaration=True, encoding="UTF-8", standalone=True)
        audit.append({"page": page, "morph_ms": 700, "matched_object_names": len(names),
                      "reveal_targets": revealed, "reveal_delays_ms": [150, 700, 1250] if revealed else []})
    target.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(target, "w") as archive:
        for entry in entries:
            archive.writestr(entry, content[entry.filename])
    report_path.write_text(json.dumps({"effects": sorted(audit, key=lambda row: row["page"]),
                                      "reveal_mode": "automatic staggered annotation groups on slide entry"},
                                     ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"output": str(target.resolve()), "morph_slides": len(audit), "reveal_groups": 3}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    for name in ["source", "target", "hints", "report"]:
        parser.add_argument(name, type=Path)
    args = parser.parse_args()
    main(args.source, args.target, args.hints, args.report)
