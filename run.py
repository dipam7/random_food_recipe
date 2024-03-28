import argparse
from pprint import pprint
from scripts.openai_client import OpenaiClient
from scripts.youtube_client import YouTubeClient
from scripts.data_model import FoodRecipes

def infer(playlist_url):
    oai_client = OpenaiClient()
    oai_client.setup_chat_client(model="gpt-3.5-turbo", response_model=FoodRecipes)

    yt_client = YouTubeClient()
    video_ids = yt_client.get_video_ids(args.playlist_url)
    transcripts = yt_client.get_transcripts(video_ids)

    for transcript in transcripts:
        messages = [
            {"role": "user", "content": f"Extract recipes from this transcript {transcript}"}
        ]
        recipes = oai_client.call_chat_client(messages).model_dump()['recipes']
        for recipe in recipes:
            pprint(recipe)
        break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--playlist_url", type=str, help="URL of the YouTube playlist")
    args = parser.parse_args()

    infer(args.playlist_url)