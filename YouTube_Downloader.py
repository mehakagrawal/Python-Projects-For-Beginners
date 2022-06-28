from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('600x400')
root.resizable(0, 0)
root.title("Mehak YouTube Video Downloader")

Label(root, text="YouTube Video Downloader", font='arial 30 bold').pack()

link = StringVar

Label(root, text="Paste the link of YouTube video here", font='arial 15 bold').place(x = 100, y = 60)

link_enter = Entry(root, width=80, textvariable=link).place(x = 32, y = 90)

def download():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text="The video is downloaded!", font='arial 15').place(x =120, y = 210)

Button(root, text="Download", font='arial 15 bold', bg = 'red', padx=2, command=download).place(x = 180, y = 150)

root.mainloop()