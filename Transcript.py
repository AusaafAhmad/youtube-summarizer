import os
import subprocess
from youtube_transcript_api._api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled 
from youtube_transcript_api.formatters import TextFormatter
import whisper

def get_videoid(link: str)-> str:
    return link.split("=")[-1]

def downloader_mp3(link: str) -> None:
    output = "downloads"

    file = os.path.join(output, f"{get_videoid(link)}.wav")

    if not os.path.exists(file):
        print(f"File doesn't Exists,Downloading \n{file}")
        command = [
        "yt-dlp",
        "-x",
        "--audio-format", "wav",
        "-o", os.path.join(output, "%(id)s.%(ext)s"),
        link
        ]
        try:
            print("Downloading and converting to wav...")
            subprocess.run(command, check=True)
            print("Download complete.")
        except subprocess.CalledProcessError as e:
            print("An error occurred:", e)
        
    return file

def transcribe_mp3(link: str) -> None:
    file = downloader_mp3(link)
    print(f"Transcribing audio: {file}")
    model = whisper.load_model("base")
    result = model.transcribe(file)
    print("Transcription complete.")
    return result["text"]


def get_transcript(link: str) -> str | Exception :
    ytt_api = YouTubeTranscriptApi()
    video_id = get_videoid(link)
    try:
        fetched = ytt_api.fetch(video_id)
        return TextFormatter().format_transcript(fetched)

    except TranscriptsDisabled:
        print("Transcripts Not found!!\nManually Transcribing!!")
        return transcribe_mp3(link)