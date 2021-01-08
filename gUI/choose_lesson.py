from tkinter import *


def callChk():
    str = "选择了"
    if v1.get() == 1:
        str += "计算机！"
    if v2.get() == 1:
        str += "自动化！"
    if v3.get() == 1:
        str += "通信工程！"
    Label(w, text=str).pack()


w = Tk()
w.geometry("250x120")
w.title("复选框操作演示")
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v1.set(1)  # 设置复选框的状态
v2.set(0)
v3.set(1)
Checkbutton(w, variable=v1, text='计算机', command=callChk).pack()
Checkbutton(w, variable=v2, text='自动化', command=callChk).pack()
Checkbutton(w, variable=v3, text='通信工程', command=callChk).pack()

w.mainloop()
