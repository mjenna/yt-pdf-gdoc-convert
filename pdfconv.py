from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import re
import yt

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
        
    remove_brackets= re.sub(r"\[.*?\]", "", transcript_text)
    cleaned_text = re.sub(r'\d{1,4}\.\d{1,3}:\s*', '', remove_brackets)
    paragraph_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    hyphen_clean =  re.sub(r"\s-\s", " ", paragraph_text)
    # words = hyphen_clean.split()
    # chunk_size = 150  # Approximate words per 10 lines (adjust as needed)
    # formatted_text = "\n\t".join([" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)])
    return hyphen_clean

def save_to_file(text, output_file="cleaned.txt"):
    """Saves the cleaned text to a file."""
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)

input_file = "transcript.txt"
cleaned_text = cleaned(input_file)
save_to_file(cleaned_text)
create_pdf_from_file("cleaned.txt")


# def cleaned(file_path, interval=5):
#     """Reads a text file, removes timestamps and bracketed text, and formats it into paragraphs every N lines."""
#     with open(file_path, "r", encoding="utf-8-sig", errors="replace") as file:
#         transcript_text = file.read()
    
#     # Remove bracketed text (e.g., "[A little upset]")
#     transcript_text = re.sub(r"\[.*?\]", "", transcript_text)
    
#     # Remove timestamps (e.g., "136.284:" or "12.34:")
#     cleaned_text = re.sub(r'\d{1,4}\.\d{1,3}:\s*', '', transcript_text)

#     # Split text into lines and remove empty ones
#     lines = [line.strip() for line in cleaned_text.split("\n") if line.strip()]
    
#     # Group lines into paragraphs of specified interval
#     paragraphs = [" ".join(lines[i:i+interval]) for i in range(0, len(lines), interval)]
    
#     # Join paragraphs with double newlines for readability
#     formatted_text = "\n\n".join(paragraphs)
    
#     return formatted_text