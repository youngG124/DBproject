from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter.ttk as ttk

def insert1():
    student_ID = e_id.get()
    student_name = e_name.get()
    age = e_age.get()
    textbook = e_textbook.get()

    if(student_ID=="" or student_name=="" or age=="") :
        MessageBox.showinfo("Insert Status", "All fields are required")
    else :
        con = mysql.connect(host="localhost", user="root", password="sky1575!!", database="english_school")
        cursor = con.cursor()
        cursor.execute("insert into student(student_id, student_name, age, textbook) values('"+ student_ID +"', '"+ student_name + "', '"+ age +"', '"+ textbook +"')")
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_age.delete(0, 'end')
        show()
        MessageBox.showinfo("Insert Status", "Inserted Succesfully")
        con.close()

def delete() :
    if(e_id.get() == ""):
        MessageBox.showinfo("Delete Status", "ID is compolsary for delete")
    else :
        con = mysql.connect(host="localhost", user="root", password="sky1575!!", database="english_school")
        cursor = con.cursor()
        cursor.execute("delete from student where student_ID ='"+ e_id.get() +"'")
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_age.delete(0, 'end')
        show()
        MessageBox.showinfo("Delete Status", "Deleted Succesfully")
        con.close()

def update() :
    student_ID = e_id.get()
    student_name = e_name.get()
    age = e_age.get()
    # textbook = e_textbook.get()

    if(student_ID=="" or student_name=="" or age=="") :
        MessageBox.showinfo("Update Status", "All fields are required")
    else :
        con = mysql.connect(host="localhost", user="root", password="sky1575!!", database="english_school")
        cursor = con.cursor()
        cursor.execute("update student set student_name = '"+ student_name +"', age = '"+ age +"' where student_ID = '"+ student_ID +"'")
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_age.delete(0, 'end')
        show()
        MessageBox.showinfo("Update Status", "Updated Succesfully")
        con.close()


def get() :
    if(e_id.get() == ""):
        MessageBox.showinfo("Fetch Status", "ID is compolsary for delete")
    else :
        con = mysql.connect(host="localhost", user="root", password="sky1575!!", database="english_school")
        cursor = con.cursor()
        cursor.execute("select * from student where student_ID ='"+ e_id.get() +"'")
        rows = cursor.fetchall()

        for row in rows:
            e_name.insert(0, row[1])
            e_age.insert(0, row[2])
        con.close()

def show() :
    con = mysql.connect(host="localhost", user="root", password="sky1575!!", database="english_school")
    cursor = con.cursor()
    cursor.execute("select * from student")
    rows = cursor.fetchall()
    list.delete(0, list.size())
    for row in rows:
        insertData = str(row[0]) + '     ' + row[1] + '     ' + str(row[2]) + '     ' + str(row[3])
        list.insert(list.size()+1, insertData)

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

    # 교재 선택하는 리스트 만들기
    con = mysql.connect(host="localhost", user="root", password="sky1575!!", database="english_school")
    cursor = con.cursor()
    cursor.execute("select bookname from textbook")
    values = [item[0] for item in cursor.fetchall()] # 이 방법 사용해서 {}를 제외한 교재의 이름만 추출하여 values에 저장
    e_textbook = ttk.Combobox(win1, height = 5, values = values)
    e_textbook.pack()
    e_textbook.set("교재 선택")
    e_textbook.place(x = 100, y = 120)

    e_class_ID = Entry()
    e_class_ID.place(x = 100, y = 150)

    insert = Button(win1, text="insert", font=('italic', 10), bg = 'white', command=insert1)
    insert.place(x = 20, y = 190)

    delete = Button(win1, text="delete", font=("italic", 10), bg="white", command=delete)
    delete.place(x = 70, y = 190)

    update = Button(win1, text="update", font=("italic", 10), bg="white", command = update)
    update.place(x = 122.5, y = 190)

    get = Button(win1, text="get", font=("italic", 10), bg="white", command = get)
    get.place(x = 181, y = 190)


    # 학생정보 리스트박스
    list = Listbox(win1, width = 40)

    list.place(x=290, y = 30)
    list.winfo_width = 600
    show()

    win1.mainloop()