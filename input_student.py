from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

# 학생 등록 창
def student_register() :
    win1 = Tk()
    win1.geometry("600x300")
    win1.title("student register")

    id = Label(win1, text = "id", font = ('bold', 10))
    id.place(x = 20, y = 30)
    name = Label(win1, text = "name", font = ('bold', 10))
    name.place(x = 20, y = 60)
    age = Label(win1, text = "age", font = ('bold', 10))
    age.place(x = 20, y = 90)
    textbook = Label(win1, text = "textbook", font = ('bold', 10))
    textbook.place(x = 20, y = 120)
    class_ID = Label(win1, text = "class", font = ('bold', 10))
    class_ID.place(x = 20, y = 150)

    e_id = Entry()
    e_id.place(x = 100, y = 30)
    e_name = Entry()
    e_name.place(x = 100, y = 60)
    e_age = Entry()
    e_age.place(x = 100, y = 90)
    e_textbook = Entry()
    e_textbook.place(x = 100, y = 120)
    e_class_ID = Entry()
    e_class_ID.place(x = 100, y = 150)

    insert = Button(win1, text="insert", font=('italic', 10), bg = 'white', command=insert)
    insert.place(x = 20, y = 140)

    win1.mainloop()

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


if __name__ == "__main__" :
    student_register()



