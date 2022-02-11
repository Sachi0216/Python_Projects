import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf','myPhoto.jpg')

conn = sqlite3.connect("list.db")

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
     ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_filename TEXT \
     )")
# Used list compprehension to be able to create a new list displaying txt from the list
    fileList = ["information.docx","Hello.txt","myImage.png", "myMovie.mpg", "World.txt", "data.pdf","myPhoto.jpg"]
    
    newList = [x for x in fileList if 'txt' in x]

    print(newList)
    