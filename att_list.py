from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter.ttk as ttk

def show() :
    con = mysql.connect(host="localhost", user="root", password="sky1575!!", database="english_school")
    cursor = con.cursor()
    cursor.execute("select s.student_name, a.a_time, t.teacher_name \
        from student s, attendance a, teacher t \
            where s.student_id = a.student_id \
                and t.teacher_id = a.check_teacher")
    rows = cursor.fetchall()
    list.delete(0, list.size())
    for row in rows :
        insertData = str(row[0]) + '    ' + str(row[1]) + '    ' + row[2]
        list.insert(list.size()+1, insertData)

    con.close()


if __name__ == "__main__" :
    attlist = Tk()
    attlist.geometry("500x300")
    attlist.title("attendance list")


    list = Listbox(attlist, width = 45)
    list.pack(pady = 15)

    show()
    attlist.mainloop()