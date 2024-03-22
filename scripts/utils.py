from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

def get_youtube_transcript(video_url):
    
    # Extract video ID from URL
    if 'youtu.be' in video_url:
        video_id = video_url.split('/')[-1]
    else:
        video_id = video_url.split('v=')[1].split('&')[0]
    # Fetch the transcript
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        # Combine transcript into a single string
        transcript_text = ' '.join([i['text'] for i in transcript])
    except TranscriptsDisabled:
        return f"Could not retrieve a transcript for the video {video_url}. Subtitles are disabled for this video."
    return transcript_text