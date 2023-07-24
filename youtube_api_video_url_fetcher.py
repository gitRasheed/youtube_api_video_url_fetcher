import os
from googleapiclient.discovery import build

# Set API key
api_key = 'YOUR_API_KEY'

# Get first x videos in channel
def get_first_x_videos_in_channel(channel_id, num_videos):

    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        part="id",
        channelId=channel_id,
        maxResults=min(num_videos, 50),  # maximum allowed by API
        type="video"
    )

    while request is not None and num_videos > 0:
        response = request.execute()
        for item in response['items']:
            print("https://www.youtube.com/watch?v=" + item['id']['videoId'])
            num_videos -= 1
            if num_videos == 0:
                return

        request = youtube.search().list_next(request, response)

# Get all videos in channel
def get_all_videos_in_channel(channel_id):

    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        part="id",
        channelId=channel_id,
        maxResults=50,  # maximum allowed by API
        type="video"
    )

    while request is not None:
        response = request.execute()
        for item in response['items']:
            print("https://www.youtube.com/watch?v=" + item['id']['videoId'])
        
        request = youtube.search().list_next(request, response)


get_all_videos_in_channel("channel_id")
