"""Set anonymous, readable PDF metadata without changing page content."""
from pathlib import Path
from pypdf import PdfReader, PdfWriter

root = Path(__file__).resolve().parent
target = root / "output/final-report-2026-10-20.pdf"
reader = PdfReader(target)
writer = PdfWriter()
writer.clone_document_from_reader(reader)
writer.add_metadata({
    "/Title": "公募基金本地LLM应用与部署研究",
    "/Author": "Intern",
    "/Subject": "最终汇报：34页正文与8页附录，2026年10月20日",
})
temporary = root / "build/pdf-with-metadata.pdf"
with temporary.open("wb") as stream:
    writer.write(stream)
temporary.replace(target)
