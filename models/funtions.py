import random
from models.utils import Utils
from halo import Halo
from docx import Document
from openpyxl import Workbook
from pptx import Presentation
from fpdf import FPDF
from PIL import Image

# =========================
# Generators
# =========================
class Funtions():
    def generate_txt(filename, target_size):
        with Halo(text="📄 Generating TXT...", spinner="dots"):
            with open(filename, "w", encoding="utf-8") as f:
                f.write(Utils.generate_random_text(100))
            Utils.pad_file_to_exact_size(filename, target_size)

    def generate_docx(filename, target_size):
        with Halo(text="📄 Generating DOCX...", spinner="dots"):
            doc = Document()
            doc.add_paragraph("Test document")
            doc.save(filename)
            Utils.pad_file_to_exact_size(filename, target_size)

    def generate_xlsx(filename, target_size):
        with Halo(text="📊 Generating XLSX...", spinner="dots"):
            wb = Workbook()
            ws = wb.active
            ws.append(["Test"])
            wb.save(filename)
            Utils.pad_file_to_exact_size(filename, target_size)

    def generate_pptx(filename, target_size):
        with Halo(text="📽️ Generating PPTX...", spinner="dots"):
            prs = Presentation()
            slide = prs.slides.add_slide(prs.slide_layouts[5])
            title = slide.shapes.title
            if title:
                title.text = "..."
            prs.save(filename)
            Utils.pad_file_to_exact_size(filename, target_size)

    def generate_pdf(filename, target_size):
        with Halo(text="📑 Generating PDF...", spinner="dots"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(0, 10, "Test PDF")
            pdf.output(filename)
            Utils.pad_file_to_exact_size(filename, target_size)

    def generate_image(filename, target_size):
        with Halo(text="🖼️ Generating PNG...", spinner="dots"):
            img = Image.new(
                "RGB",
                (256, 256),
                color=(
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                )
            )
            img.save(filename, format="PNG")
            Utils.pad_file_to_exact_size(filename, target_size)
