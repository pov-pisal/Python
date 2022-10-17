from os import path
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil

#Funtions
def select_path():
    #allows user to select a path from the exlorer
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title('Downloadind....')
    #Download Video
    mp4_Video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_Video)
    vid_clip.close()
    #move file to selected directory
    shutil.move(mp4_Video, user_path)
    screen.title('Download Complete! Download Another file....')

screen = Tk()
title = screen.title('Youtube Downloaad By: POV PISAL')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#image logo
logo_img = PhotoImage(file='Yt.png1.png')
#resize
logo_img = logo_img.subsample(3,3)
canvas.create_image(250, 80, image=logo_img)

#link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter Download Link: ", font=('Aril', 15) )

#select Path for saving the file
path_label = Label(screen, text="Select Path For Download", font=('Aril', 15) )
secet_btn = Button (screen, text="Setect", command=select_path)
#Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=secet_btn)

#Add widgets to window
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)


#Download btns
download_btn = Button(screen, text="Download File", command=download_file)
#add to canvas
canvas.create_window(250, 390, window=download_btn)

screen.mainloop()

#Finally
#Sunday,16,2022