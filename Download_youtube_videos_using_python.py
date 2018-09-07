import pytube
link =input("place youtube link here to download in your computer:\n")
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()
try:
    print("Downloading starts...\n")
    print("Download completed..!!")
except Exception as e:
    print(e)
