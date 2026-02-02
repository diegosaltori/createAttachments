import os
import datetime
from models.utils import Utils
from models.funtions import Funtions
from models.banners import Banners

# =========================
# Main
# =========================

def main():
    Banners.print_banner()
    Banners.print_info()

    while True: 
        # =========================
        # Unit selection
        # =========================
        while True:
            unit = input(
                "Choose the size unit KB or MB (type 'exit' to quit): "
            ).strip().upper()

            if unit == "EXIT":
                print("👋 Exiting Create Attachments. Bye!")
                return

            if unit in {"KB", "MB"}:
                break

            print("❌ Invalid unit! Please choose KB or MB.")

        # =========================
        # Size input
        # =========================
        try:
            raw_size = input("Enter the file size: ").strip().replace(",", ".")

            if unit == "KB":
                if "." in raw_size:
                    print("❌ KB only accepts integer values (e.g., 10 KB).")
                    continue  
                size = int(raw_size)
            else:  # MB
                size = float(raw_size)

        except ValueError:
            print("❌ Invalid size value!")
            continue

        if size <= 0:
            print("❌ Size must be greater than 0!")
            continue

        # =========================
        # Convert to bytes
        # =========================
        target_size_bytes = (
            size * 1024 if unit == "KB"
            else int(size * 1024 * 1024)
        )

        # =========================
        # File type
        # =========================
        file_type = input(
            "Choose the file type (txt, docx, xlsx, pptx, pdf, img): "
        ).strip().lower()

        generators = {
            "txt": Funtions.generate_txt,
            "docx": Funtions.generate_docx,
            "xlsx": Funtions.generate_xlsx,
            "pptx": Funtions.generate_pptx,
            "pdf": Funtions.generate_pdf,
            "img": Funtions.generate_image,
        }

        if file_type not in generators:
            print("❌ Invalid file type!")
            continue

        # =========================
        # File creation
        # =========================
        directory = Utils.ensure_directory()
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

        extension = "png" if file_type == "img" else file_type
        filename = os.path.join(
            directory,
            f"documentTest_{size}{unit}_{timestamp}.{extension}"
        )

        try:
            generators[file_type](filename, target_size_bytes)
            print("🎉 File generated successfully!")
            print(f"📦 Final size: {os.path.getsize(filename)} bytes")
            print()  
        except Exception as e:
            print(f"❌ Error: {e}")
            continue

if __name__ == "__main__":
    main()
