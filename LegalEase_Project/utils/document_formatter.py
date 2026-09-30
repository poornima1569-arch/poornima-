from io import BytesIO
import re
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from fpdf import FPDF


def sanitize_text(text: str) -> str:
    replacements = {
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2013": "-",
        "\u2014": "-",
        "\u00a0": " ",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text.strip()


def format_txt(text: str) -> bytes:
    return sanitize_text(text).encode("utf-8")


def _setup_docx(document, doc_type):
    section = document.sections[0]
    section.top_margin = Inches(0.7)
    section.bottom_margin = Inches(0.7)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)

    style = document.styles["Normal"]
    style.font.name = "Times New Roman"
    style.font.size = Pt(11)

    title = document.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run(doc_type.upper())
    run.bold = True
    run.font.name = "Times New Roman"
    run.font.size = Pt(16)

    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer.add_run("Generated with LegalEase | AI-assisted draft | Review before use")


def format_docx(text: str, doc_type: str) -> bytes:
    document = Document()
    _setup_docx(document, doc_type)

    for raw in sanitize_text(text).splitlines():
        line = raw.strip()
        if not line:
            document.add_paragraph()
            continue

        p = document.add_paragraph()
        if (
            line.isupper()
            or re.match(r"^\d+[\.\)]\s+", line)
            or line.endswith(":")
        ):
            r = p.add_run(line)
            r.bold = True
        else:
            p.add_run(line)

    output = BytesIO()
    document.save(output)
    return output.getvalue()


class LegalEasePDF(FPDF):
    def __init__(self, doc_type):
        super().__init__()
        self.doc_type = doc_type
        self.set_auto_page_break(auto=True, margin=18)

    def header(self):
        self.set_font("Helvetica", "B", 13)
        self.cell(0, 8, "LegalEase", align="C")
        self.ln(7)
        self.set_font("Helvetica", "B", 11)
        self.cell(0, 6, self.doc_type.upper(), align="C")
        self.ln(8)

    def footer(self):
        self.set_y(-14)
        self.set_font("Helvetica", size=8)
        self.cell(0, 8, "LegalEase | AI-assisted draft | Review before use", align="C")


def format_pdf(text: str, doc_type: str) -> bytes:
    pdf = LegalEasePDF(doc_type)
    pdf.add_page()
    pdf.set_font("Helvetica", size=10)

    for raw in sanitize_text(text).splitlines():
        line = raw.strip()
        if not line:
            pdf.ln(4)
            continue

        pdf.set_x(pdf.l_margin)
        if line.isupper() or re.match(r"^\d+[\.\)]\s+", line):
            pdf.set_font("Helvetica", "B", 10)
            pdf.multi_cell(0, 6, line)
            pdf.set_font("Helvetica", size=10)
        else:
            pdf.set_x(pdf.l_margin)
            pdf.multi_cell(0, 5.5, line)

    return bytes(pdf.output(dest="S"))
