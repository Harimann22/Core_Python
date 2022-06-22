from pytube import YouTube
# SAVE_PATH = "F:/"
# link = "https://www.youtube.com/watch?v=mF2BHtQh4EI"
# try:
#     yt = YouTube(link)
# except:
#     print("Connection Error")
# mp4files = yt.streams.filter("mp4")
# yt.set_filename('new Video')
# d_video = yt.get(mp4files[-1].extention, mp4files[-1].resolution)
# try:
#     d_video.download(SAVE_PATH)
# except:
#     print("Some Error")
# print("Task Complite")

link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

# Showing details
print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length)
print("Rating of video: ", yt.rating)
# Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

# Starting download
print("Downloading...")
ys.download()
print("Download completed!!")
