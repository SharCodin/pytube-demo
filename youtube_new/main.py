"""Main entry point of application."""

import json
import re

import youtube_api_v3 as yt
from extracts.subscription import channels
from settings import API_KEY

for channel_id in channels:
    print(channel_id)
    youtube = yt.YouTube(channel_id, API_KEY)
    response = youtube.get_channel_data()
    output_json = json.loads(response.text)
    file_name = output_json["items"][0]["snippet"]["title"].replace(" ", "_").lower()
    file_name = re.sub(r"\W", "_", file_name)
    print(file_name)
    with open(f"extracts/z_{file_name}.json", "w", encoding="utf-8") as f:
        f.write(response.text)
