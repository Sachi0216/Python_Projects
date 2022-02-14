
from cgitb import text
import tkinter
from tkinter import *
from tkinter.tix import TEXT

import webbrowser

from tkinter import *
root = Tk()
root.geometry("500x500")
# Button for browser/html file
def open_browser():
    webbrowser.open_new("file:///Users/elijahdavis/basicwebpage.html")

browser_button = Button(root, text="Open Browser", font=("Helvectica", 34), command=open_browser)
# Open new tab in url to display results for new body
browser_button.pack(pady=50)
def open_new_tab():
    webbrowser.open_new_tab("file:///Users/elijahdavis/basicwebpage.html")
# input button and label to change the body of the url
input_label = Button(text="Input", font=("Helvectica", 24), fg="blue", command=text)

input_label.pack(padx=20,pady=20)
# open the new tab after displaying text results
f = open("Basicwebpage.html", "w")
f.write("Text")
f.close()

f = open("Basicwebpage.html", "r")
print(f.read())
    

if __name__ =="__main__":
    root.mainloop()
    root.title('Google.com - Open web browser')
    
    