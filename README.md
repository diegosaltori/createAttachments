# Attachment Test File Generator

This script generates test documents of various types (TXT, DOCX, XLSX, PPTX, PDF, and Images) with an exact and deterministic file size.
The file size can be defined in KB or MB, and the script guarantees the final size in bytes, regardless of file format or compression.

## Features
- Generate files with an **exact size in bytes**.
- Size unit selection:
  - **KB** → integer values only
  - **MB** → integer or float values (e.g. 5.1 MB)
- Interactive CLI mode (generate multiple files in one execution).
- Type `exit` at any prompt to quit the script.
- Supports TXT, DOCX, XLSX, PPTX, PDF, and PNG image files.
- Visual feedback with spinners and emojis.

---

##### **Note:**
File generation time may increase for very large files.
The script uses a binary padding strategy to ensure exact file size, avoiding inconsistencies caused by compression or metadata.

---

## Supported File Types
- **TXT**: Text file with random content.
- **DOCX**: Word document with paragraphs of random text.
- **XLSX**: Excel file with random text in cells.
- **PPTX**: PowerPoint file with slides containing random text.
- **PDF**: PDF file with pages filled with random text.
- **Image**: PNG image with random colors.

---

## 🚀 How to Use

### 1️⃣ Clone or download the repository

You can either **download the ZIP** or **clone using Git**:

**Download ZIP**

```
https://github.com/diegosaltori/createAttachments/archive/refs/heads/main.zip
```

**Clone with Git**

```bash
git clone https://github.com/diegosaltori/createAttachments.git
```

Then access the project folder:

```bash
cd createAttachments
```

---

### 2️⃣ Install the required dependencies

Make sure you have **Python 3.8+** installed.

Install all dependencies using `pip`:

```bash
pip install halo python-docx openpyxl python-pptx fpdf pillow
```

> 💡 Tip: You can also install them one by one if needed:

```bash
pip install halo
pip install python-docx
pip install openpyxl
pip install python-pptx
pip install fpdf
pip install pillow
```

---

### 3️⃣ Run the script

Execute the script with Python:

```bash
python createAttachments.py
```

Follow the on-screen instructions to choose:

* File size unit (KB or MB)
* File size
* File type (txt, docx, xlsx, pptx, pdf, img)

---

## ⚙️ How the Script Works

When you run the script, it interacts with you via the terminal and guides you step by step to generate a file with an **exact size in bytes**, based on your input.

### 🔹 User Inputs

During execution, you will be prompted to provide the following information:

1. **Size unit (KB or MB)**  
   Defines how the file size will be calculated.

   - `KB` → Integer values only (e.g. `10 KB`)
   - `MB` → Integer or floating-point values (e.g. `5 MB`, `5.1 MB`)

2. **File size**
   The numeric value for the selected unit.

   Examples:
   - `10` + `MB` → exactly 10 MB
   - `5.1` + `MB` → exactly 5.1 MB
   - `256` + `KB` → exactly 256 KB

3. **File type**
   Choose one of the supported formats:
   - `txt`, `docx`, `xlsx`, `pptx`, `pdf`, `img`

---

## 🧠 Internal Behavior

After receiving the input, the script:

1. Creates a **valid minimal file** for the chosen format.
2. Converts the user-defined size into **exact bytes** using base 1024.
3. Applies a **binary padding strategy** to reach the exact target size.
4. Ensures the final file size matches the requested value precisely.
5. Returns to the initial prompt, allowing the user to generate additional files.

This approach guarantees deterministic file sizes and avoids issues caused by compression or internal metadata.

## 🔁 Interactive Mode

The script runs in an interactive loop.

- After generating a file, it returns to the size unit selection.
- You can generate multiple files in a single execution.
- Type `exit` at any prompt to terminate the script gracefully.

---

## 📌 Example Execution

```text
Choose the size unit KB or MB (type 'exit' to quit): MB
Enter the file size: 5.1
Choose the file type (txt, docx, xlsx, pptx, pdf, img): pptx
📽️ Generating PPTX...
🎉 File generated successfully!
📦 Final size: 5347737 bytes

Choose the size unit KB or MB (type 'exit' to quit):
```

## 📁 Output

- All generated files are saved in the `attachmentsTest` directory.
- Files are named using the following pattern:

```
documentTest_{size}{unit}_{timestamp}.{extension}
```

**Example:**

```
documentTest_4000KB_20260129123045.pdf
```

## Directory Structure

```
createAttachments/
│
├── createAttachments.py  # The main script file.
└── attachmentsTest/      # The folder where generated files will be stored.
```

## Requirements

- Python 3.x
- Libraries: `halo`, `python-docx`, `openpyxl`, `python-pptx`, `fpdf`, `pillow`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
