import sqlite3

# connecting to sqlite3 database project1.db
conn = sqlite3.connect('project2.db')

with conn:
    cur = conn.cursor()
    # Create table in database if not present.
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileType(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_type TEXT)")
    conn.commit()



conn = sqlite3.connect('project2.db')

# tuple of files
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


# loop through each object in the tuple to find the files that end in .txt.
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
        # The value for each row will be one name out of the tuple therefore (x,)
        #will denote a one element tuple for each file ending with txt. 
            cur.execute("INSERT INTO tbl_fileType (col_type) VALUES (?)", (x,))
            print(x)


conn.close()