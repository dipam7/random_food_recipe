from loguru import logger
from openai import OpenAI
from instructor import patch
from .data_model import FoodRecipes
from functools import partial

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

def get_youtube_transcript(video_url):
    if 'youtu.be' in video_url:
        video_id = video_url.split('/')[-1]
    else:
        video_id = video_url.split('v=')[1].split('&')[0]
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ' '.join([i['text'] for i in transcript])
    except TranscriptsDisabled:
        logger.warning(f"Could not retrieve a transcript for the video {video_url}. Subtitles are disabled for this video.")
        return None
    return transcript_text

def setup_openai_client(api_key):
    client = patch(OpenAI(api_key=api_key))

    chat_client = partial(client.chat.completions.create, model="gpt-3.5-turbo", response_model=FoodRecipes)
    return chat_client

def call_openai_client(chat_client, transcript):
    op = chat_client(
        messages=[
            {"role": "user", "content": f"Extract recipes from this transcript {transcript}"}]
    )
    return op.model_dump()['recipes']