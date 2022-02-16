from pathlib import Path
import shutil
import os
from tkinter import *
from tkinter import filedialog
# allows users to open file folder and choose files/add new/search
def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\BigDipper6969\\OneDrive\\Desktop\\Daily projects",
                                          title="Open file okay?",
                                          filetypes= (("Daily files","*.txt"),
                                          ("all files","*.*")))
    file = open(filepath,'r')
    print(file.read())
    file.close()

window = Tk()
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()


# set where the source of the files are
source = "\\Users\\BigDipper6969\\OneDrive\\Desktop\\folderA"

# set destination path to folder b
destination = "\\Users\\BigDipper6969\\OneDrive\\Desktop\\folderB"
files = os.listdir(source)


for i in files:
    shutil.move(source, destination)