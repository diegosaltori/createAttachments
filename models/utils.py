import os
import random
import string

# =========================
# Utils
# =========================
class Utils(): 
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
                f"File already larger than desired size."
                f"({current_size} > {target_size_bytes})"
            )

        with open(filename, "ab") as f:
            f.write(b'\0' * (target_size_bytes - current_size))
            