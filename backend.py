from sqlite3 import *

#Creates a table with a specific name if it doensnt already exist
def create_table():
    connec = connect("books.db")
    curr = connec.cursor()

    curr.execute("CREATE TABLE IF NOT EXISTS bookstore (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")

    connec.commit()
    connec.close()

#Allows you to view db contents
def view_all ():
    connec = connect("books.db")
    curr = connec.cursor()

    curr.execute("SELECT * FROM bookstore")

    rows = curr.fetchall()

    connec.close()
    return rows

#Search Function, that searches for parameter, thern displays it 
def Search_Entry(title, author, year, isbn): 
    connec = connect("books.db")
    curr = connec.cursor()

    curr.execute("SELECT * FROM bookstore WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
    row = curr.fetchall()

    connec.close()  
    return row  

##Insert function
def Add_Entry(title, author, year, isbn):
    connec = connect("books.db")
    curr = connec.cursor()

    curr.execute("INSERT INTO bookstore VALUES(NULL, ?, ?, ?, ?)", (title, author, year, isbn))

    connec.commit()
    connec.close()

#Updates existing values in a db
def update(id, title, author, year, isbn):
    connec = connect("books.db")
    curr = connec.cursor()

    curr.execute("UPDATE bookstore SET title =?, author =?, year =?, isbn =? WHERE id =? ", (title, author, year, isbn, id))

    connec.commit()
    connec.close()

#Deleted selected row in the db
def Delete_Selected(id): 
    connec = connect("books.db")
    curr = connec.cursor()

    curr.execute("DELETE FROM bookstore WHERE id =?", (id,))

    connec.commit()
    connec.close()


