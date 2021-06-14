from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter.ttk as ttk

if __name__ == "__main__" :
    atcheckwin = Tk()
    atcheckwin.geometry("300x400")
    atcheckwin.title("attendance check")

    # 출석 체크하는 선생님 선택하는 리스트 만들기
    con = mysql.connect(host="localhost", user="root", password="sky1575!!", database="english_school")
    cursor = con.cursor()
    cursor.execute("select teacher_name from teacher")
    # 선생님 이름만 콤보박스에 저장
    teachernames = [item[0] for item in cursor.fetchall()]
    teacher = ttk.Combobox(atcheckwin, width = 15, height = 5, values = teachernames)
    teacher.pack()
    teacher.set("확인 선생님")
    teacher.pack(pady=15)

    # 학생들 목록
    s_list = Listbox(atcheckwin, width = 15)
    s_list.pack(pady = 15)
    cursor.execute("select student_name from student")
    rows = cursor.fetchall()
    s_list.delete(0, s_list.size())
    for row in rows:
        insertData = str(row[0])
        s_list.insert(s_list.size()+1, insertData)

    temperature = Entry()
    temperature.pack(pady = 5)

    # 출석체크 버튼
    def check() :
        con = mysql.connect(host="localhost", user="root", password="sky1575!!", database="english_school")
        cursor = con.cursor()

        # 리스트박스의 학생 이름으로 학생 id 가져오기.
        cursor.execute("select student_ID from student where student_name = '" + s_list.get(ANCHOR) + "'")
        s_id = [item[0] for item in cursor.fetchall()] # s_id[0] 으로 id만 가져올 수 있음.
        s_id2 = str(s_id[0])
        # 콤보박스의 선생님 이름으로 선생님 id 가져오기.
        cursor.execute("select teacher_ID from teacher where teacher_name = '" + teacher.get() + "'")
        t_id = [item[0] for item in cursor.fetchall()] # t_id[0] 으로 id만 가져올 수 있음.
        t_id2 = str(t_id[0])
        # 체온 빈칸에서 체온 가져오기.
        temperature2 = temperature.get()

        cursor.execute("insert into attendance(student_ID, temperature, check_teacher)\
            values('"+ s_id2 + "', '" + temperature2 + "', '" + t_id2 + "')")
        cursor.execute("commit")

        MessageBox.showinfo("attendance check", "attendance checked!")
        con.close()


    check_button = Button(atcheckwin, text="check", command = check)
    check_button.pack(pady = 10)

    con.close()
    atcheckwin.mainloop()