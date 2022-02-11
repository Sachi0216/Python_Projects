import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf','myPhoto.jpg')

conn = sqlite3.connect('people.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_people( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_email TEXT, \
        col_phonenumber \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('people.db')


with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_people(col_fname, col_lname, col_email, col_phonenumber) VALUES (?,?,?,?)", \
                ('Elijah', 'Davis', 'edavis@gmail.com', '123-4567'))
    cur.execute("INSERT INTO tbl_people(col_fname, col_lname, col_email, col_phonenumber) VALUES (?,?,?,?)", \
                ('Anakin', 'Skywalker', 'skywalker1@gmail.com','123-4567'))
    cur.execute("INSERT INTO tbl_people(col_fname, col_lname, col_email, col_phonenumber) VALUES (?,?,?,?)", \
                ('Luke', 'Skywalker', 'skywalker2@gmail.com','123-4567'))
    conn.commit()
conn.close()



conn = sqlite3.connect('people.db')


with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname,col_lname,col_email,col_phonenumber FROM tbl_people WHERE col_fname = 'Elijah'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First Name: {}\nLast Name: {}\nEmail: {}\nPhone Number: {}".format(item[0],item[1],item[2],item[3])
    print(msg)
