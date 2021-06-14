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
                and t.teacher_id = a.check_teacher \
                    and date(a_time) = date(now())")
    rows = cursor.fetchall()
    list.delete(0, list.size())
    for row in rows :
        insertData = str(row[0]) + '    ' + str(row[1]) + '    ' + row[2]
        list.insert(list.size()+1, insertData)

    con.close()

def search() :
    student_name = student_combo.get()

    con = mysql.connect(host="localhost", user="root", password="sky1575!!", database="english_school")
    cursor = con.cursor()
    cursor.execute("select s.student_name, a.a_time, t.teacher_name \
        from student s, attendance a, teacher t \
            where s.student_id = a.student_id \
                and t.teacher_id = a.check_teacher \
                    and s.student_name = '" + student_name + "'")
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

    # 학생 이름 불러오기
    con = mysql.connect(host="localhost", user="root", \
         password="sky1575!!", database="english_school")
    cursor = con.cursor()
    cursor.execute("select student_name from student")
    students = [item[0] for item in cursor.fetchall()]
    # 불러온 이름 콤보박스에 넣기
    student_combo = ttk.Combobox(attlist, height = 5, values = students)
    student_combo.pack(pady = 15)
    student_combo.set("학생 선택")
    # 검색 버튼
    search = Button(attlist, text="검색", font=('italic', 10), bg = 'white', command = search)
    search.pack(pady = 1)

    list = Listbox(attlist, width = 35)
    list.pack(pady = 15)

    show()
    attlist.mainloop()