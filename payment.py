from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter.ttk as ttk

def show_student() :
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
    payment = Tk()
    payment.geometry("300x330")
    payment.title("payment")

    # 출석 체크하는 선생님 선택하는 리스트 만들기
    

    # 학생들 목록
    s_list = Listbox(payment, width = 15)
    s_list.pack(pady = 5)
    
    show_student()

    t_label = Label(payment, text = "결제 금액", font = ('bold', 10))
    t_label.pack(pady=5)

    pay_amount = Entry()
    pay_amount.pack(pady = 10)


    # 출석체크 버튼
    def pay() :
        if(pay_amount.get()=="" or s_list.get(ANCHOR)=="") :
            MessageBox.showinfo("Insert Status", "All fields are required")
        else :
            con = mysql.connect(host="localhost", user="root", password="sky1575!!", database="english_school")
            cursor = con.cursor()

            # 리스트박스의 학생 이름으로 학생 id 가져오기.
            cursor.execute("select student_ID from student \
                where student_name = '" + s_list.get(ANCHOR) + "'")
            s_id = [item[0] for item in cursor.fetchall()] # s_id[0] 으로 id만 가져올 수 있음.
            s_id2 = str(s_id[0])
            # 체온 빈칸에서 체온 가져오기.
            pay_amount2 = pay_amount.get()

            cursor.execute("insert into payment\
                (student_ID, pay_amount)\
                values('"+ s_id2 + "', '" + pay_amount2 + "')")
            cursor.execute("commit")

            MessageBox.showinfo("payment", "paid Succesfully")
            con.close()


    check_button = Button(payment, text="check", command = pay)
    check_button.pack(pady = 10)

    refresh = Button(payment, text="refresh", command = show_student)
    refresh.pack(pady = 10)


    payment.mainloop()