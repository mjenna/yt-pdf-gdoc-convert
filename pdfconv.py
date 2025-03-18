from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf_from_file(filename):
    #read transcript text from file
    with open(filename, "r") as file:
        transcript_text = file.read()

    #create a PDF doc
    pdf_filename = "transcript.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    width, height = letter

    #adds the transcript text to PDF
    c.setFont("Helvetica", 10)
    c.drawString(100, height - 100, transcript_text)
    c.save()

    print(f"PDF created: {pdf_filename}")

create_pdf_from_file("transcript.txt")