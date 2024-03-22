import argparse
from scripts.utils import get_youtube_transcript

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch YouTube video transcript")
    parser.add_argument("-v", "--video_url", type=str, help="URL of the YouTube video")
    args = parser.parse_args()
    
    transcript = get_youtube_transcript(args.video_url)
    print(transcript)
