import argparse, os
from pprint import pprint
from scripts.utils import get_youtube_transcript, setup_openai_client, call_openai_client
from dotenv import load_dotenv

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--video_url", type=str, help="URL of the YouTube video")
    args = parser.parse_args()

    load_dotenv(override=True)
    api_key = os.environ['OPENAI_API_KEY']
    
    transcript = get_youtube_transcript(args.video_url)
    chat_client = setup_openai_client(api_key)
    recipes = call_openai_client(chat_client, transcript)
    for recipe in recipes:
        pprint(recipe)