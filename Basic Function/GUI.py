import tkinter
import tkinter.messagebox
from tkinter import ttk
from tkinter import StringVar
from tkinter import Toplevel
# def event1(): 
#     tkinter.messagebox.showinfo('messagebox', '정보가 있습니다.') # 정보를 알리는 용도의 파란 원에 느낌표 아이콘
#     tkinter.messagebox.showwarning('messagebox', '문제가 있습니다.') # 위험을 알리는 노란 세모에 느낌표 아이콘
#     tkinter.messagebox.showerror('messagebox', '에러가 있습니다.') # 오류를 알리는 빨간 원에 X표 아이콘
# def event2(): # 확인 취소를 묻는 메세지 박스
#     tkinter.messagebox.askokcancel('messagebox', '확인 or 취소를 선택해주세요.')
    
# def event3(): # 대답을 묻는 메세지 박스
#     tkinter.messagebox.askquestion('messagebox', '예 or 아니오를 선택해주세요.')
#     tkinter.messagebox.askyesno('messagebox', '예 or 아니오를 선택해주세요.')
#     tkinter.messagebox.askyesnocancel('messagebox', '예 or 아니오 or 취소를 선택해주세요.')
# def event4():
#     tkinter.messagebox.askretrycancel('messagebox', '다시시도 하시겠습니까?') # 다시하기 버튼
# GUI = tkinter.Tk() # GUI 생성
# GUI.title('GUI Test!') # GUI 창 타이틀
# GUI.geometry('720x480') # GUI 크기 조절    
# GUI.resizable(False, False) # GUI 창 크기를 조절 가능 여부

# GUI의 내부 옵션들의 위치를 설정하는 방법은 두 가지가 있다.
# 첫 번째 grid는 행, 열 값
# lbl.tkinter.Label(GUI, text='name')
# lbl.grid(row=400, column=300)

# 두 번째 place는 좌표 값
# tkinter.Label(GUI, text='name').place(x=30, y=40) # tkinter.Label: 글자를 입력
# tkinter.Entry(GUI).place(x=35,y=30) # 입력창
# tkinter.Button(GUI, text='button', command=event1).place(x=50, y=60)
# tkinter.Button(GUI, text='button', command=event2).place(x=30, y=70)
# tkinter.Button(GUI, text='button', command=event3).place(x=30, y=80)
# tkinter.Button(GUI, text='button', command=event4).place(x=30, y=90)

# 세 번쨰 pack는 한 블록씩 점유




def add_list():
    def list_append():
        name = add_name.get() # <textvariable name>.get()을 통해 Entry에 입력한 값을 가져옴
        age = add_age.get()
        major = add_major.get()
        ai_dic = {
            'name' : name,
            'age' : age,
            'major' : major
        }
        ai_list.append(ai_dic)
        name1.delete(0,'end')
        age1.delete(0,'end')
        major1.delete(0,'end')

    add = Toplevel(GUI) # 기존의 GUI에 새로운 GUI를 실행하게 되면 기존의 GUI가 먼저이기 때문에 .get을 할 때 먼저 실행한 GUI에서 가져오기 때문에 새로운 GUI의 entry에 입력한 값을 가져올 수가 없다.
    # 하지만 Toplevel은 응용프로그램 창이기 때문에 닫으면 정보는 삭제되지만 프로그램이 종료되지는 않는다.
    add.title('Add List')
    add.geometry('250x180')
    
    tkinter.Label(add, text='name').place(x=25, y=30)
    name1 = tkinter.Entry(add, textvariable = add_name)
    name1.place(x=65, y=30)
    name1.focus()

    tkinter.Label(add, text='age').place(x=25, y=60)
    age1 = tkinter.Entry(add, textvariable = add_age)
    age1.place(x=65, y=60)

    tkinter.Label(add, text='major').place(x=25, y=90)
    major1 = tkinter.Entry(add, textvariable = add_major)
    major1.place(x=65, y=90)

    tkinter.Button(add, text='OK', command=list_append, width=5, height=1).place(x=130, y=130)
    tkinter.Button(add, text='Close', command=add.destroy, width=5, height=1).place(x=170, y=130)

    

def view():
    for i in ai_list:
        print('{} {} {}'.format(i['name'], i['age'], i['major']))
    for i in ai_list:
        treeview.insert('', 'end', value=(i['name'], i['age'], i['major']))
GUI = tkinter.Tk()
GUI.title('GUI Test!')
GUI.geometry('720x600')
GUI.resizable(False, False) # GUI 창 크기를 조절 가능 여부

ai_list = []
ai_dic = {}

add_name = StringVar() # StringVar는 반드시 Tk() 뒤에 입력해야 한다. (마스터가 필요)
add_age = StringVar() # StringVar는 Entry에 입력한 값을 불러오기 위해 사용
add_major = StringVar()

tkinter.Button(GUI, text='Add List', command=add_list, width=10, height=3).place(x=480, y=500)
tkinter.Button(GUI, text='View', command=view, width=10, height=3).place(x=570, y=500)



treeview = ttk.Treeview(GUI, columns=['name', 'age', 'major'], height=20) # treeview는 행렬로 나뉘어진 표를 생성
treeview.place(x=50, y=50)
treeview.column("name", width=200, anchor="center") # column명과 너비, 글자 위치 선택
treeview.heading("name", text='name', anchor="center")

treeview.column("age", width=100, anchor="center") # column명과 너비, 글자 위치 선택
treeview.heading("age", text='age', anchor="center")

treeview.column("major", width=300, anchor="center") # column명과 너비, 글자 위치 선택
treeview.heading("major", text='major', anchor="center")

treeview['show']='headings' # 표 가장 앞 빈 공간을 없애줄 수 있다. head 부분을 지워준다.


GUI.mainloop() # GUI를 실행하고 종료되지 않도록 잡아주는 역할