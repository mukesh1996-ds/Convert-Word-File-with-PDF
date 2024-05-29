
```markdown
# Word to PDF Converter

This project provides a user interface for converting Word documents to PDF using Gradio. The interface allows users to upload a Word document and receive a PDF version of the document.

## Project Description

The goal of this project is to create a simple and intuitive user interface using Gradio for converting Word documents (.docx) to PDF format. This tool can be useful for users who need a quick and easy way to convert their Word documents without installing additional software.

## Features

- Upload a Word document (.docx) file.
- Convert the uploaded document to a PDF file.
- Display the conversion status to the user.

## Requirements

- Python 3.7+
- Gradio
- transformers
- python-docx
- reportlab

## Installation

1. Clone the repository:

```bash
git clone https://github.com/mukesh1996-ds/Convert-Word-File-with-PDF.git
cd word-to-pdf-converter
```

2. Install the required Python packages:

```bash
pip install gradio transformers python-docx reportlab
```

## Usage

1. Run the application:

```bash
python app.py
```

2. Open your web browser and go to the URL provided in the terminal output (usually `http://127.0.0.1:7860`).

3. Upload your Word document (.docx) and wait for the conversion to complete.

4. Download the converted PDF file.

## Code Overview

### `app.py`

This is the main script that defines the Gradio interface and handles the conversion process.

```python
import gradio as gr
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def convert_word_to_pdf(input_path, output_path):
    doc = Document(input_path)
    pdf = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    y = height - 40
    for para in doc.paragraphs:
        text = para.text
        pdf.drawString(40, y, text)
        y -= 14
        if y < 40:
            pdf.showPage()
            y = height - 40

    pdf.save()

def gradio_convert_word_to_pdf(file):
    input_path = file.name
    output_path = os.path.splitext(input_path)[0] + ".pdf"
    convert_word_to_pdf(input_path, output_path)
    return "Conversion successful! Output saved as: " + output_path

app = gr.Interface(
    fn=gradio_convert_word_to_pdf,
    inputs=gr.File(label="Input Word Document"),
    outputs=gr.Textbox(label="Conversion status"),
    live=True,
    title="Word To PDF Converter",
    description="Convert word document to PDF"
)

app.launch()
```

## Thanks 
