from youtube_transcript_api import YouTubeTranscriptApi
import sys
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import re

video_url = input("Paste URL of the YouTube video: ").strip()

#extracts video id
video_id = video_url.split("v=")[1].split("&")[0]

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
except Exception as e:
    print(f"Cannot get the transcript: {e}")
    sys.exit(1)

#print transcript into a text file
with open("transcript.txt", "w") as file:
    for entry in transcript:
        file.write(f"{entry['start']}: {entry['text']}\n")

video_url = input("Paste URL of the YouTube video: ").strip()
yes_stamp = input("Include timestamps? (yes/no): ").strip().lower()

if yes_stamp in ["yes", "y"]:
    video_url = input("Paste the URL of the YouTube video: ").strip()
    print(f"You entered: {video_url}")
else:
    print("No URL provided. Exiting...")

