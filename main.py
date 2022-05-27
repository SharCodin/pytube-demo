"""Get information about a YouTube Channel using the YouTube API."""

from typing import Any
from pytube import Channel, YouTube  # type: ignore
import pandas
import datetime

masterlist: list[dict[str, str]] = []

c: Any = Channel('https://www.youtube.com/c/AdobeVideo/videos')


def main(stopper: int):
    """Run when the app starts."""
    file_name: str | None = None
    for index, item in enumerate(c):
        if index > stopper:
            break

        masterdict: dict[str, Any] = {}

        yt: Any = YouTube(item)
        title: Any = yt.title

        if not file_name:
            file_name = yt.author.replace(' ', '_')

        print(index, title)

        masterdict['title'] = title
        masterdict['minutes'] = str(datetime.timedelta(seconds=yt.length))
        masterdict['date'] = yt.publish_date
        masterdict['views'] = yt.views
        masterdict['url'] = item
        masterdict['description'] = yt.description

        masterlist.append(masterdict)

    df = pandas.DataFrame(masterlist)
    df.to_csv(f'{file_name}_data.csv', ';', index=False)  # type: ignore


if __name__ == "__main__":
    main(366)
