# I use this program so that I can watch youtube vidoes on a plane or any situation that i would not be connected to the internet.

from pytube import YouTube

mylink = input("link: ")
yt = YouTube(mylink)

###print("Title: ", yt.title)

yd = yt.streams.get_highest_resolution()
yd.download('/Users/DV0095/Documents/Python Projects/YT Videos')
print("DONE!")