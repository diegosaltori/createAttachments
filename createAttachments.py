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

def generate_random_text(size):
    return ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=size))

def ensure_directory():
    directory = "attachmentsTest"
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def generate_txt(filename, size):
    with Halo(text='📄 Generating TXT file...', spinner='dots') as spinner:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(generate_random_text(size))
        spinner.succeed("✅ TXT file generated!")

def generate_docx(filename, size):
    with Halo(text='📄 Generating DOCX file...', spinner='dots') as spinner:
        doc = Document()
        doc.save(filename)  # Creating the file before checking size
        while os.path.getsize(filename) < size:
            doc.add_paragraph(generate_random_text(1024))
            doc.save(filename)
        spinner.succeed("✅ DOCX file generated!")

def generate_xlsx(filename, size):
    with Halo(text='📊 Generating XLSX file...', spinner='dots') as spinner:
        wb = Workbook()
        ws = wb.active
        wb.save(filename)  # Creating the file before checking size
        while os.path.getsize(filename) < size:
            for _ in range(100):
                ws.append([generate_random_text(50)])
            wb.save(filename)
        spinner.succeed("✅ XLSX file generated!")

def generate_pptx(filename, size):
    with Halo(text='📽️ Generating PPTX file...', spinner='dots') as spinner:
        prs = Presentation()
        prs.save(filename)  # Creating the file before checking size
        while os.path.getsize(filename) < size:
            slide = prs.slides.add_slide(prs.slide_layouts[5])
            textbox = slide.shapes.add_textbox(100, 100, 500, 500)
            textbox.text = generate_random_text(1024)
            prs.save(filename)
        spinner.succeed("✅ PPTX file generated!")

def generate_pdf(filename, size):
    with Halo(text='📑 Generating PDF file...', spinner='dots') as spinner:
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=10)
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.output(filename)  # Creating the file before checking size
        while os.path.getsize(filename) < size:
            pdf.add_page()
            pdf.multi_cell(0, 10, generate_random_text(1024))
            pdf.output(filename)
        spinner.succeed("✅ PDF file generated!")

def generate_image(filename, target_size_bytes):
    with Halo(text='🖼️ Generating image...', spinner='dots') as spinner:
        # Start with a large image size to accommodate the target size
        width, height = 1024, 1024  # Initial size of the image
        img = Image.new('RGB', (width, height), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        # Add random noise to the image
        pixels = img.load()
        for i in range(img.width):
            for j in range(img.height):
                pixels[i, j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Save the image
        img.save(filename, format="PNG")
        
        # Check if the size is smaller than the target, and if so, increase the image size and add more data
        while os.path.getsize(filename) < target_size_bytes:
            width += 128  # Increase the width
            height += 128  # Increase the height
            img = img.resize((width, height))

            # Add more noise to the resized image
            pixels = img.load()
            for i in range(img.width):
                for j in range(img.height):
                    pixels[i, j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            # Save the image after resizing and adding noise
            img.save(filename, format="PNG")

        spinner.succeed(f"✅ Image generated with size: {os.path.getsize(filename) / 1024:.2f} KB")

def main():
    unit = input("Choose the size unit (KB/MB): ").strip().upper()
    if unit not in ["KB", "MB"]:
        print("❌ Invalid unit!")
        return
    
    size = int(input("Enter the file size (>= 0): "))
    if size < 0:
        print("❌ Size must be greater than or equal to 0!")
        return
    
    file_type = input("Choose the file type (txt, docx, xlsx, pptx, pdf, img): ").strip().lower()
    supported_types = {"txt", "docx", "xlsx", "pptx", "pdf", "img"}
    if file_type not in supported_types:
        print("❌ Invalid file type!")
        return
    
    size_bytes = size * 1024 if unit == "KB" else size * 1024 * 1024
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    directory = ensure_directory()
    
    # Modify filename to ensure it's a .png for images
    if file_type == "img":
        filename = os.path.join(directory, f"documentTest_{size}{unit}_{timestamp}.png")
    else:
        filename = os.path.join(directory, f"documentTest_{size}{unit}_{timestamp}.{file_type}")
    
    if file_type == "txt":
        generate_txt(filename, size_bytes)
    elif file_type == "docx":
        generate_docx(filename, size_bytes)
    elif file_type == "xlsx":
        generate_xlsx(filename, size_bytes)
    elif file_type == "pptx":
        generate_pptx(filename, size_bytes)
    elif file_type == "pdf":
        generate_pdf(filename, size_bytes)
    elif file_type == "img":
        generate_image(filename, size_bytes // 1024)
    
    print(f"🎉 File {filename} generated successfully!")

if __name__ == "__main__":
    main()
