
import tkinter as tk
from tkinter import *

import webbrowser
#
root = tk.Tk()

def openBrowser():
    f = open("Basicwebpage.html", 'w')
    text = myEntryLbl.get()
    f.write(text)
    webbrowser.open_new("Basicwebpage.html")



myEntryLbl = tk.Label(root, text="Enter some text here.")
myEntryLbl.grid(row=0,column=0, padx=(160,0), pady=(20,0), sticky=NSEW)
myEntryLbl.grid_rowconfigure(0, weight=1)

myEntryLbl = tk.Entry(root, text='')
myEntryLbl.grid_rowconfigure(0, weight=1)
myEntryLbl.grid(row=2,columnspan=160, padx=(160,0), pady=(20,0))

input_button = Button(text="Generate", font=("Helvectica", 34), command=openBrowser)
input_button.grid(padx=20, pady=20)

root.mainloop()