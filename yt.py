from youtube_transcript_api import YouTubeTranscriptApi
import sys
import re

if __name__ == "__main__":
    video_url = input("Paste URL of the YouTube video: ").strip()

    #extracts video id
    match = re.search(r"v=([^&]+)", video_url)

    if match:
        video_id = match.group(1)
    else:
        print("Cannot find video ID. Exiting...")

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except Exception as e:
        print(f"Cannot get the transcript: {e}")
        sys.exit(1)

    #print transcript into a text file
    with open("transcript.txt", "w") as file:
        for entry in transcript:
            file.write(f"{entry['start']}: {entry['text']}\n")
