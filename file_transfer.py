from distutils import filelist
from pathlib import Path
import tkinter as tk
import shutil
import os
from tkinter import *
from tkinter import filedialog
import tkinter

from numpy import absolute

    
window = Tk()
window.title('Files')
window.geometry("200x120")

# widgets
label = tkinter.Label(window, text="Source")
sourceEntry = tkinter.Entry(window)

labelTransfer = tkinter.Label(window, text="Destination")
destEntry = tkinter.Entry(window)

button1 = tkinter.Button(window, text="Source", command=lambda:sourcefolder())
button2 = tkinter.Button(window, text="Destination", command=lambda:destFolder())
button = tkinter.Button(window, text="Move", command=lambda:transferfiles())

label.pack()
sourceEntry.pack()
labelTransfer.pack()
destEntry.pack()
button.pack()
button1.pack()
button2.pack()

def sourcefolder():
    src = filedialog.askdirectory()
    sourceEntry.insert(0, src)

def destFolder():
    dest = filedialog.askdirectory()
    destEntry.insert(0, dest)

def transferfiles():
    src = sourceEntry.get()
    dest = destEntry.get()
    fileList = os.listdir(src) 

    for file in fileList:
        absolutePath = os.path.join(src, file)
        shutil.move(absolutePath, dest)
window.mainloop()

# source = "\\Users\\BigDipper6969\\OneDrive\\Desktop\\folderA"

# # set destination path to folder b

# destination = "\\Users\\BigDipper6969\\OneDrive\\Desktop\\folderB"
# files = os.listdir(source)


# for i in files:
#     shutil.move(source, destination)




# root.mainloop()