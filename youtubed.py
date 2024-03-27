from pytube import YouTube

link = input('Enter Video link: ')
yt = YouTube(link)

print("Title:", yt.title)
print("Views:", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download()
