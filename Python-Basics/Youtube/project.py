try:
    from pytube import YouTube
    from pytube import Playlist
except Exception as e:
    print("Some modules are Missing {}".format(e))

url = "https://youtube.com/watch?v=RDUsN55dbnM"
ytd = YouTube(url)
print(ytd)
ytd.streams.filter(only_audio=True).first().download()

for x in ytd.streams.all():
    print(x)