from pytube import Channel, YouTube


c = Channel('https://www.youtube.com/channel/UCtJNlrOPYE25Th5ATbgpoow')
for item in c:
    yt = YouTube(item)
    print(yt.author)
    print(yt.description)
    print(yt.length / 60)
    print(yt.publish_date)
    print(yt.title)
    print(yt.views)
    break
