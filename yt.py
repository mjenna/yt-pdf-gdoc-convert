from youtube_transcript_api import YouTubeTranscriptApi
import sys

#handling multiple URLs
video_urls = input("Paste URLs of the YT videos (separated by commas if multiple): ").strip().split(",")

with open("transcript.txt", "w") as file:
    for index, video_url in enumerate(video_urls, 1): #process each video URL
        video_url = video_url.strip()  #removes any white space
        try:
            video_id = video_url.split("v=")[1].split("&")[0] #extract video ID from the URL
            transcript = YouTubeTranscriptApi.get_transcript(video_id) #grab the transcript for the current video ID
            file.write(f"Transcript for Video {index}\n")  #transcript for video into file: labeling as Video 1, Video 2...
            
            for entry in transcript:
                file.write(f"{entry['start']}: {entry['text']}\n")
            
            file.write("\n")  #add a blank line after each transcript

            print(f"Transcript for Video {index} added to transcript.txt")

        except Exception as e:
            file.write(f"Cannot get the transcript for {video_url}: {e}\n\n")
            print(f"Cannot get the transcript for {video_url}: {e}")

print("All transcripts have been saved in transcript.txt")
