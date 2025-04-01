# Test Document Generator Script

This script generates test documents of various types (TXT, DOCX, XLSX, PPTX, PDF, and Images) with a customizable file size. The file can be generated in either KB or MB units. The generated file will be saved in the `attachmentsTest` directory with a unique name based on the size and current timestamp.

## Features
- Choose the desired file size in KB or MB.
- Choose the file type (TXT, DOCX, XLSX, PPTX, PDF, or Image).
- The script will generate random content in the file until it reaches the specified size.
- Emojis and loading indicators are displayed for better user experience.

---

##### **Note:** The larger the file size, the longer it will take to generate the file. Larger files require more time to create due to the increased amount of content being written.

---

## Supported File Types
- **TXT**: Text file with random content.
- **DOCX**: Word document with paragraphs of random text.
- **XLSX**: Excel file with random text in cells.
- **PPTX**: PowerPoint file with slides containing random text.
- **PDF**: PDF file with pages filled with random text.
- **Image**: PNG image with random colors.

## How to Use

1. Clone or download this repository.
2. Install the required libraries:
   - `pip install halo`
   - `pip install python-docx`
   - `pip install openpyxl`
   - `pip install python-pptx`
   - `pip install fpdf`
   - `pip install pillow`
3. Run the script using Python:
   - `python createAttachments.py`

## Interaction

When running the script, you will be prompted to provide the following inputs:
1. **Choose the size unit (KB/MB)**: Select between KB or MB to define the file size.
2. **Enter the file size (>= 0)**: Enter the size of the file you wish to generate (must be >= 0).
3. **Choose the file type (txt, docx, xlsx, pptx, pdf, img)**: Select the type of file you want to generate.

The script will then generate the file with random content until the specified size is reached. It will display a loading indicator and success message with an emoji for better feedback.

## Example Output

```
Choose the size unit (KB/MB): KB
Enter the file size (>= 0): 4000
Choose the file type (txt, docx, xlsx, pptx, pdf, img): pdf
📑 Generating PDF file... ✅ PDF file generated!
🎉 File attachmentsTest/documentTest_4000KB_20250401120313.pdf generated successfully!
```

The file will be saved in the `attachmentsTest` directory with the name `documentTest_{size}{unit}_{timestamp}.{file_type}`.

## Directory Structure

```
your_project_directory/
│
├── createAttachments.py  # The main script file.
└── attachmentsTest/      # The folder where generated files will be stored.
```

## Requirements

- Python 3.x
- Libraries: `halo`, `python-docx`, `openpyxl`, `python-pptx`, `fpdf`, `pillow`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
