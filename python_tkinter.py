from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def insert():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if(id=="" or name=="" or phone=="") :
        MessageBox.showinfo("Insert Status", "All fields are required")
    else :
        con = mysql.connect(host="localhost", user="root", password="sky1575!!", database="python_tkinter")
        cursor = con.cursor()
        cursor.execute("insert into student values('"+ id +"', '"+ name + "', '"+ phone +"')")
        cursor.execute("commit")
        show()
        MessageBox.showinfo("Insert Status", "Inserted Succesfully")
        con.close()

def delete() :
    if(e_id.get =="") :
        MessageBox.showinfo("Delete Status", "ID is compolsary for delete")
    else :
        con = mysql.connect(host="localhost", user="root", password="sky1575!!", database="python_tkinter")
        cursor = con.cursor()
        cursor.execute("delete from student where id = '"+ e_id.get() + "'")
        cursor.execute("commit")
        show()
        MessageBox.showinfo("Delete Status", "Deleted Succesfully")
        con.close()

def update() :
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if(id=="" or name=="" or phone=="") :
        MessageBox.showinfo("Update Status", "All fields are required")
    else :
        con = mysql.connect(host="localhost", user="root", password="sky1575!!", database="python_tkinter")
        cursor = con.cursor()
        cursor.execute("update student set name='"+ name +"', phone='"+ phone +"' where id='"+ id +"'")
        cursor.execute("commit")
        show()
        MessageBox.showinfo("Update Status", "Updated Succesfully")
        con.close()

def get():
    if(e_id.get =="") :
        MessageBox.showinfo("Fetch Status", "ID is compolsary for delete")
    else :
        con = mysql.connect(host="localhost", user="root", password="sky1575!!", database="python_tkinter")
        cursor = con.cursor()
        cursor.execute("select * from student where id='"+ e_id.get() + "'")
        rows = cursor.fetchall()

        for row in rows :
            e_name.insert(0, row[1])
            e_phone.insert(0, row[2])
            
        con.close()

def show():
    con = mysql.connect(host="localhost", user="root", password="sky1575!!", database="python_tkinter")
    cursor = con.cursor()
    cursor.execute("select * from student")
    rows = cursor.fetchall()
    list.delete(0, list.size())

    for row in rows :
        insertData = str(row[0]) + '          ' + row[1]
        list.insert(list.size() + 1, insertData)

    con.close()

def open_another_window() :
    root2 = Tk()
    root2.title("another window")



root = Tk() # make window
root.geometry("600x300")
root.title("tkinter + mysql")

id = Label(root, text = 'ENTER ID', font = ('bold', 10))
id.place(x = 20, y = 30)

name = Label(root, text = 'ENTER NAME', font = ('bold', 10))
name.place(x = 20, y = 60)

phone = Label(root, text = 'ENTER PHONE', font = ('bold', 10))
phone.place(x = 20, y = 90)

e_id = Entry()
e_id.place(x=180, y = 30)

e_name = Entry()
e_name.place(x=180, y = 60)

e_phone = Entry()
e_phone.place(x=180, y = 90)

insert = Button(root, text="insert", font=('italic', 10), bg = 'white', command=insert)
insert.place(x = 20, y = 140)

delete = Button(root, text="delete", font=('italic', 10), bg = 'white', command=delete)
delete.place(x = 70, y = 140)

update = Button(root, text="update", font=('italic', 10), bg = 'white', command=update)
update.place(x = 130, y = 140)

get = Button(root, text="get", font=('italic', 10), bg = 'white', command=get)
get.place(x = 190, y = 140)

open = Button(root, text="open", font=('italic', 10), bg = 'white', command=open_another_window)
open.place(x = 250, y = 140)

list = Listbox(root)
list.place(x = 350, y = 30)
show()

root.mainloop()

