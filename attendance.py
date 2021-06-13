from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter.ttk as ttk

def show() :
    con = mysql.connect(host="localhost", user="root", password="sky1575!!", database="english_school")
    cursor = con.cursor()
    cursor.execute("select student_name from student")
    rows = cursor.fetchall()
    s_list.delete(0, s_list.size())
    for row in rows:
        insertData = str(row[0])
        s_list.insert(s_list.size()+1, insertData)

    con.close()

if __name__ == "__main__" :
    atcheckwin = Tk()
    atcheckwin.geometry("600x300")
    atcheckwin.title("attendance check")

    s_list = Listbox(atcheckwin)
    s_list.pack(pady = 15)
    
    show()

    atcheckwin.mainloop()