from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql





def insert1():
    student_ID = e_id.get()
    student_name = e_name.get()
    age = e_age.get()
    textbook = e_textbook.get()
    class_ID = e_class_ID.get()

    if(student_ID=="" or student_name=="" or age=="") :
        MessageBox.showinfo("Insert Status", "All fields are required")
    else :
        con = mysql.connect(host="localhost", user="root", password="sky1575!!", database="english_school")
        cursor = con.cursor()
        cursor.execute("insert into student(student_ID, student_name, age, textbook) values('"+ student_ID +"', '"+ student_name + "', '"+ age +"', '"+ textbook +"')")
        cursor.execute("commit")
        MessageBox.showinfo("Insert Status", "Inserted Succesfully")
        con.close()



if __name__ == "__main__" :
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

    insert = Button(win1, text="insert", font=('italic', 10), bg = 'white', command=insert1)
    insert.place(x = 20, y = 190)

    win1.mainloop()


