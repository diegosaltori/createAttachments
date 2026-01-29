import os
import random
import string
import datetime
from halo import Halo
from docx import Document
from openpyxl import Workbook
from pptx import Presentation
from fpdf import FPDF
from PIL import Image


# =========================
# Utils
# =========================

def ensure_directory():
    directory = "attachmentsTest"
    os.makedirs(directory, exist_ok=True)
    return directory


def generate_random_text(size):
    return ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=size))


def pad_file_to_exact_size(filename, target_size_bytes):
    current_size = os.path.getsize(filename)

    if current_size > target_size_bytes:
        raise ValueError(
            f"Arquivo já maior que o tamanho desejado "
            f"({current_size} > {target_size_bytes})"
        )

    with open(filename, "ab") as f:
        f.write(b'\0' * (target_size_bytes - current_size))


# =========================
# Generators
# =========================

def generate_txt(filename, target_size):
    with Halo(text="📄 Generating TXT...", spinner="dots"):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(generate_random_text(100))
        pad_file_to_exact_size(filename, target_size)


def generate_docx(filename, target_size):
    with Halo(text="📄 Generating DOCX...", spinner="dots"):
        doc = Document()
        doc.add_paragraph("Test document")
        doc.save(filename)
        pad_file_to_exact_size(filename, target_size)


def generate_xlsx(filename, target_size):
    with Halo(text="📊 Generating XLSX...", spinner="dots"):
        wb = Workbook()
        ws = wb.active
        ws.append(["Test"])
        wb.save(filename)
        pad_file_to_exact_size(filename, target_size)


def generate_pptx(filename, target_size):
    with Halo(text="📽️ Generating PPTX...", spinner="dots"):
        prs = Presentation()
        slide = prs.slides.add_slide(prs.slide_layouts[5])
        slide.shapes.title = None
        prs.save(filename)
        pad_file_to_exact_size(filename, target_size)


def generate_pdf(filename, target_size):
    with Halo(text="📑 Generating PDF...", spinner="dots"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, "Test PDF")
        pdf.output(filename)
        pad_file_to_exact_size(filename, target_size)


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
        pad_file_to_exact_size(filename, target_size)


# =========================
# Main
# =========================

def main():
    unit = input("Choose the size unit (KB/MB): ").strip().upper()
    if unit not in {"KB", "MB"}:
        print("❌ Invalid unit!")
        return

    size = int(input("Enter the file size (>= 1): "))
    if size < 1:
        print("❌ Size must be >= 1!")
        return

    file_type = input(
        "Choose the file type (txt, docx, xlsx, pptx, pdf, img): "
    ).strip().lower()

    generators = {
        "txt": generate_txt,
        "docx": generate_docx,
        "xlsx": generate_xlsx,
        "pptx": generate_pptx,
        "pdf": generate_pdf,
        "img": generate_image,
    }

    if file_type not in generators:
        print("❌ Invalid file type!")
        return

    target_size_bytes = size * 1024 if unit == "KB" else size * 1024 * 1024

    directory = ensure_directory()
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    extension = "png" if file_type == "img" else file_type
    filename = os.path.join(
        directory,
        f"documentTest_{size}{unit}_{timestamp}.{extension}"
    )

    try:
        generators[file_type](filename, target_size_bytes)
        print(f"🎉 File generated successfully!")
        print(f"📦 Final size: {os.path.getsize(filename)} bytes")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
