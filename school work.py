# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 10:39:05 2023

@author: lucas
"""
import threading
from pytube import YouTube
import tkinter as tk

def showProgress():
    pass

def onClick():

    global var
    var.set(entry.get())
    
    button.config(state=tk.DISABLED)
    try:
        yt = YouTube(var.get(),
                     on_progress_callback=showProgress)
        if onlyMusic.get():
            stream = yt.streams.filter(only_audio=True).first()
        else:
            stream = yt.streams.filter(res="720p").first()
        
        stream.download()
    except:
        print("download fail")
        button.config(state=tk.NORMAL)
        
def thread():
    threading.Thread(target=onClick).start()
    
        
window = tk.Tk()
window.title("youtube downloader")
window.geometry("500x150")
window.resizable(False,False)

scale = tk.Scale(window,label="progress", from_=0, to=100,
                 orient=tk.HORIZONTAL,
                 length=200, showvalue=False,
                 tickinterval=0)
scale.pack()


onlyMusic = tk.BooleanVar()
check = tk.Checkbutton(window, text = "only music", variable = onlyMusic,
                                onvalue = True,offvalue = False)
check.pack()

label = tk.Label(window,
                 text = "pls enter Youtube video address")
label.pack()

var = tk.StringVar()
entry = tk.Entry(window, width = 50)
entry.pack()

button = tk.Button(window, text = "download",
                   command = thread)
button.pack()
window.mainloop()