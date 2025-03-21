from youtube_transcript_api import YouTubeTranscriptApi
import sys


#handling multiple URLS
video_urls = input("Paste URLs of the YT video (separated by commas if multiple): ").strip().split(",")

#video_url = input("Paste URL of the YouTube video: ").strip()

#extracts video id
#video_id = video_url.split("v=")[1].split("&")[0]
for video_url in video_urls:
    video_url = video_url.strip() #remove any white space
    video_id = video_url.split("v=")[1].split("&")[0] #extract video id

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
except Exception as e:
    print(f"Cannot get the transcript: {e}")
    sys.exit(1)

#print transcripts into text files
transcript_filename = f"transcript_{video_id}.txt"
with open("transcript.txt", "w") as file:
    for entry in transcript:
        file.write(f"{entry['start']}: {entry['text']}\n")



