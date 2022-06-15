"""Main entry point of application."""

import json

import youtube_api_v3 as yt
from settings import API_KEY

channel_ids = [
    "UCtJNlrOPYE25Th5ATbgpoow",
    "UCovw7Ksx437NHFgGvg_tX2A",
    "UCGxjDWAN1KwrkXYVi8CXtjQ",
    "UCJQJAI7IjbLcpsjWdSzYz0Q",
    "UCE6MSh7T4B3trx3VS_uPBmA",
    "UCWPJwoVXJhv0-ucr3pUs1dA",
]

for channel_id in channel_ids:
    print(channel_id)
    youtube = yt.YouTube(channel_id, API_KEY)
    response = youtube.get_channel_data()
    output_json = json.loads(response.text)
    file_name = output_json["items"][0]["snippet"]["title"].replace(" ", "_").lower()
    print(file_name)
    with open(f"extracts/{file_name}.json", "w", encoding="utf-8") as f:
        f.write(response.text)
