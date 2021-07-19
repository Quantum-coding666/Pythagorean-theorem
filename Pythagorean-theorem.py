from tkinter import *
import platform
import tkinter.messagebox

if platform.system() == 'Windows':
    from tkinter.ttk import *

window = Tk()
window.title("直角三角形三边-知2求1")
window.geometry("300x200")

def clicked():
    if len(e1.get()) == 0 and len(e2.get()) > 0 and len(e3.get()) > 0:
        h=int(e3.get())*int(e3.get())-int(e2.get())*int(e2.get())
        r=h ** 0.5
        e1.insert(0,str(r))
        if r!=int(r):
            s1.configure(text="即√￣"+str(h))
    elif len(e2.get()) == 0 and len(e1.get()) > 0 and len(e3.get()) > 0:
        h=int(e3.get())*int(e3.get())-int(e1.get())*int(e1.get())
        r=h ** 0.5
        e2.insert(0,str(r))
        if r!=int(r):
            s2.configure(text="即√￣"+str(h))
    elif len(e3.get()) == 0 and len(e2.get()) > 0 and len(e1.get()) > 0:
        h=int(e1.get())*int(e1.get())+int(e2.get())*int(e2.get())
        r=h ** 0.5
        e3.insert(0,str(r))
        if r!=int(r):
            s3.configure(text="即√￣"+str(h))
    else:
        tkinter.messagebox.showerror(title='出错了！',message='您的输入格式有误，请输入两个参数，程序会自动填入第三个参数')


l1 = Label(window,text="三角形直角边1")
l1.grid(column=0, row=1)
e1 = Entry(window)
e1.grid(column=1, row=1)
s1 = Label(window, text="")
s1.grid(column=1, row=2)

l2 = Label(window,text="三角形直角边2")
l2.grid(column=0, row=3)
e2 = Entry(window)
e2.grid(column=1, row=3)
s2 = Label(window, text="")
s2.grid(column=1, row=4)

l3 = Label(window,text="三角形的斜边")
l3.grid(column=0, row=5)
e3 = Entry(window)
e3.grid(column=1, row=5)
s3 = Label(window, text="")
s3.grid(column=1, row=6)

btn = Button(window, text="计算", command=clicked)
btn.grid(column=1, row=7)

window.mainloop()