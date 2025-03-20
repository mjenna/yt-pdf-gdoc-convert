from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import re

def create_pdf_from_file(filename):
    #read transcript text from file
    with open(filename, "r") as file:
        transcript_text = file.read()

    #create a PDF doc
    pdf_filename = "transcript.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

    styles = getSampleStyleSheet()
    style_normal = styles['Normal']

    content = []
    paragraph = Paragraph(transcript_text.replace("\n", "<br />"), style_normal)
    content.append(paragraph)
    doc.build(content)

    print(f"PDF created: {pdf_filename}")

def cleaned(file_path):
    """Reads a text file, removes timestamps, and returns cleaned text."""
    with open(file_path, "r", encoding="utf-8-sig", errors="replace") as file:
        transcript_text = file.read()
    
    # Regular expression to match timestamps (e.g., 136.284: or 12.34:)
    remove_brackets= re.sub(r"\[.*?\]", "", transcript_text)
    cleaned_text = re.sub(r'\d{1,4}\.\d{1,3}:\s*', '', remove_brackets)
    
    return cleaned_text

def save_to_file(text, output_file="cleaned.txt"):
    """Saves the cleaned text to a file."""
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)

input_file = "transcript.txt"
cleaned_text = cleaned(input_file)
save_to_file(cleaned_text)
create_pdf_from_file("cleaned.txt")