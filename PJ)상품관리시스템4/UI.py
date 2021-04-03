# main과 view 파일을 UI로 대체한다.
import tkinter
import tkinter.font
from tkinter import Toplevel, StringVar, ttk
import db_controller
from domain import Entity

def gui_input(window, title):
    window.title(title)
    window.geometry('250x180')
    window.configure(background='#323435')


def insert_product():
    def list_append():
        name = input_name.get() # <textvariable name>.get()을 통해 Entry에 입력한 값을 가져옴
        price = input_price.get()
        code = input_code.get()
        color = input_color.get()
        ct.control_register(Entity(name, price, code, color))
        name1.delete(0, 'end')
        price1.delete(0, 'end')
        code1.delete(0, 'end')
        color1.delete(0, 'end')

    add = Toplevel(window)
    gui_input(add, 'Add List')

    # add = Toplevel(GUI)
    # add.title('Add List')
    # add.geometry('250x180')
    tkinter.Label(add, text='name', width=4, height=1).place(x=25, y=20)
    name1 = tkinter.Entry(add, textvariable = input_name)
    name1.place(x=65, y=20)
    name1.focus()

    tkinter.Label(add, text='price', width=4, height=1).place(x=25, y=50)
    price1 = tkinter.Entry(add, textvariable = input_price)
    price1.place(x=65, y=50)

    tkinter.Label(add, text='code', width=4, height=1).place(x=25, y=80)
    code1 = tkinter.Entry(add, textvariable = input_code)
    code1.place(x=65, y=80)

    tkinter.Label(add, text='color', width=4, height=1).place(x=25, y=110)
    color1 = tkinter.Entry(add, textvariable = input_color)
    color1.place(x=65, y=110)

    tkinter.Button(add, text='OK', command=list_append, width=5, height=1).place(x=115, y=140)
    tkinter.Button(add, text='Close', command=add.destroy, width=5, height=1).place(x=165, y=140)


def read_product():
    product_list = ct.control_get_all_entity()
    for i in treeview.get_children():
        treeview.delete(i)
    for i in product_list:
        treeview.insert('', 'end', value=(i['code'], i['name'], i['price'], i['color']))


def update_product():
    def list_update():
        code = input_code.get()
        name = input_name.get()
        price = input_price.get()
        color = input_color.get()
        ct.control_update_entity(Entity(name, price, code, color))
        code1.delete(0, 'end')
        name1.delete(0, 'end')
        price1.delete(0, 'end')
        color1.delete(0, 'end')
    update = Toplevel(window)
    gui_input(update, 'Update Lsist')

    tkinter.Label(update, text='code', width=4, heigh=1).place(x=25, y=20)
    code1 = tkinter.Entry(update, textvariable = input_code)
    code1.place(x=65, y=20)
    code1.focus()

    tkinter.Label(update, text='name', width=4, height=1).place(x=25, y=50)
    name1 = tkinter.Entry(update, textvariable = input_name)
    name1.place(x=65, y=50)

    tkinter.Label(update, text='price', width=4, height=1).place(x=25, y=80)
    price1 = tkinter.Entry(update, textvariable = input_price)
    price1.place(x=65, y=80)

    tkinter.Label(update, text='color', width=4, height=1).place(x=25, y=110)
    color1 = tkinter.Entry(update, textvariable = input_color)
    color1.place(x=65, y=110)

    tkinter.Button(update, text='OK', command=list_update, width=5, height=1).place(x=115, y=140)
    tkinter.Button(update, text='Close', command=update.destroy, width=5, height=1).place(x=165, y=140)


def delete_product():
    def list_delete():
        code = input_code.get()
        ct.control_delete_entity(code)
        code1.delete(0, 'end')
    delete = Toplevel(window)
    gui_input(delete, 'Delete List')

    tkinter.Label(delete, text='code', width=4, height=1).place(x=25, y=20)
    code1 = tkinter.Entry(delete, textvariable = input_code)
    code1.place(x=65, y=20)
    code1.focus()
    
    tkinter.Button(delete, text='OK', command=list_delete, width=5, height=1).place(x=115, y=140)
    tkinter.Button(delete, text='Close', command=delete.destroy, width=5, height=1).place(x=165, y=140)


def info_product():
    def entity_info():
        code = input_code.get()
        entity = ct.control_get_entity(code)
        for i in treeview.get_children():
            treeview.delete(i)
        treeview.insert('', 'end', value=(entity['name'], int(entity['price']), entity['color']))
        info1.delete(0, 'end')

    info = Toplevel(window)
    gui_input(info, 'Info List')

    tkinter.Label(info, text='code', width=4, height=1).place(x=25, y=20)
    info1 = tkinter.Entry(info, textvariable = input_code)
    info1.place(x=65, y=20)
    info1.focus()
    
    tkinter.Button(info, text='OK', command=entity_info, width=5, height=1).place(x=115, y=140)
    tkinter.Button(info, text='Close', command=info.destroy, width=5, height=1).place(x=165, y=140)

    treeview = ttk.Treeview(info, columns=['name', 'price', 'color'], height=3) # treeview는 행렬로 나뉘어진 표를 생성
    treeview.place(x=25, y=50)
    treeview['show']='headings'
    treeview.column("name", width=60, anchor="center")
    treeview.heading("name", text='name', anchor="center")
    treeview.column("price", width=60, anchor="center")
    treeview.heading("price", text='price', anchor="center")
    treeview.column("color", width=60, anchor="center")
    treeview.heading("color", text='color', anchor="center")


def END():
    window.destroy()
    
'''==========================================================================================='''

ct = db_controller.PRController()
# window 창 생성
window = tkinter.Tk()
window.title('Product_list_management')
window.geometry('480x720+30+30') # 화면 크기 및 위치 조정
window.resizable(False, False) # 마우스로 화면 크기 조절 x
window.configure(background='#323435')

# StringVar 생성: Label 위의 입력값을 받아 사용할 수 있다.
input_name = StringVar() # StringVar는 반드시 Tk() 뒤에 입력해야 한다. (마스터가 필요)
input_price = StringVar() # StringVar는 Entry에 입력한 값을 불러오기 위해 사용
input_code = StringVar()
input_color = StringVar()
# 메뉴바 생성
menubar = tkinter.Menu(window)
filemenu = tkinter.Menu(menubar)
filemenu.add_command(label="Create", command=insert_product)
filemenu.add_command(label="Read", command=read_product)
filemenu.add_command(label="Update", command=update_product)
filemenu.add_command(label="Delete", command=delete_product)
filemenu.add_command(label="Info", command = info_product)
filemenu.add_command(label="Exit", command=END)
menubar.add_cascade(label="File", menu=filemenu) # 하위 메뉴와 상위 메뉴를 연결
window.config(menu=menubar) # window에 menubar를 연결

# treeview 생성 (column으로 구분되어 있는 출력창)
treeview = ttk.Treeview(window, columns=['code', 'name', 'price', 'color'], height=25) # treeview는 행렬로 나뉘어진 표를 생성
treeview.place(x=35, y=20)
treeview['show']='headings' # 표 가장 앞 빈 공간을 없애줄 수 있다. head 부분을 지워준다.

# column명과 너비, 글자 위치 선택
treeview.column("code", width=100, anchor="center")
treeview.heading("code", text='code', anchor="center")
treeview.column("name", width=100, anchor="center")
treeview.heading("name", text='name', anchor="center")
treeview.column("price", width=100, anchor="center")
treeview.heading("price", text='price', anchor="center")
treeview.column("color", width=100, anchor="center")
treeview.heading("color", text='color', anchor="center")

window.mainloop()

# 추가 사항
# 잘못 입력했을 경우 messagebox를 출력하여 오류가 발생한 것을 알려준다. # control에 있는 view 모듈 삭제 (message 대신 messagebox로 대체)
# 값이 입력되었을 때 어떤 값이 입력되었다는 message를 출력될 수 있게 한다. // 기능들을 모듈에 넣고 하던가 UI에 당겨와서 해야될듯??
# read를 하였을 때 treeview에 입력된 값을 초기화하고 출력하도록 (학교 컴터에 저장된거 usb에 옮겨 담는다.)
# 오류 잡기 공백, 잘못된 타입 등을 입력하였을 떄

# db에 연결하면 domain을 사용하는지 안하는지 묻기