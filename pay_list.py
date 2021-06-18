from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter.ttk as ttk

def show_today() :
    con = mysql.connect(host="localhost", user="root", password="sky1575!!", database="english_school")
    cursor = con.cursor()
    cursor.execute("select s.student_name, p.pay_time, p.pay_amount \
        from student s, payment p \
            where s.student_ID = p.student_ID \
                and date(pay_time) = date(now()) \
                    order by pay_time asc")
    rows = cursor.fetchall()
    list.delete(0, list.size())
    for row in rows :
        insertData = str(row[0]) + '    ' + str(row[1]) + '    ' + str(row[2])
        list.insert(list.size()+1, insertData)

    con.close()

def search() :
    student_name = student_combo.get()

    con = mysql.connect(host="localhost", user="root", password="sky1575!!", database="english_school")
    cursor = con.cursor()
    cursor.execute("select s.student_name, p.pay_time, p.pay_amount \
        from student s, payment p \
            where s.student_ID = p.student_ID \
                    and s.student_name = '"+ student_name +"' \
                        order by pay_time asc")
    rows = cursor.fetchall()
    list.delete(0, list.size())
    for row in rows :
        insertData = str(row[0]) + '    ' + str(row[1]) + '    ' + str(row[2])
        list.insert(list.size()+1, insertData)

    con.close()

def delete() :
    # 리스트에서 이름만 가져오기
    a = str(list.get(ANCHOR))
    delete_name = a[0] + a[1] + a[2]

    # 리스트에서 가져온 학생 이름으로 아이디 가져오기
    con = mysql.connect(host="localhost", user="root", \
         password="sky1575!!", database="english_school")
    cursor = con.cursor()
    cursor.execute("select student_ID from student \
        where student_name = '" + delete_name + "'")
    delete_id = [item[0] for item in cursor.fetchall()]
    delete_id2 = str(delete_id[0])

    # 가져온 아이디 사용해서 삭제
    cursor.execute("delete from payment \
        where student_ID = '" + delete_id2 + "'\
            and date(pay_time) = date(now())")
    cursor.execute("commit")
    show_today()
    MessageBox.showinfo("Delete Status", "Deleted Succesfully")
    con.close()


if __name__ == "__main__" :
    pay_list = Tk()
    pay_list.geometry("315x300")
    pay_list.title("payment list")

    # 학생 이름 불러오기
    con = mysql.connect(host="localhost", user="root", password="sky1575!!", database="english_school")
    cursor = con.cursor()
    cursor.execute("select student_name from student")
    students = [item[0] for item in cursor.fetchall()]
    # 불러온 이름 콤보박스에 넣기
    student_combo = ttk.Combobox(pay_list, height = 5, values = students)
    student_combo.place(x = 30, y = 20)
    student_combo.set("학생 선택")
    # 검색 버튼
    search = Button(pay_list, text="검색", font=('italic', 10), bg = 'white', command = search)
    search.place(x = 200, y = 20)
    # 삭제 버튼
    delete = Button(pay_list, text="삭제", font=('italic', 10), bg = 'white', command = delete)
    delete.place(x = 242.5, y = 20)
    # 오늘 출석체크 확인 버튼
    today = Button(pay_list, text="오늘", font=('italic', 10), bg = 'white', command = show_today)
    today.place(x = 30, y = 70)


    list = Listbox(pay_list, width = 35)
    list.place(x = 30, y = 90)

    show_today()
    pay_list.mainloop()
