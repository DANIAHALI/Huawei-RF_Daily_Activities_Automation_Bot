from tkinter import *
import time
import main_gui_connecter
import pdb

print('Processing Start Please Wait!')
master = Tk()
master.title('RF Daily Activities Automation')
master.geometry("632x440")
master.resizable(width=False, height=False)
master.iconbitmap("Images\\huawei_icon.ico")
icon1 = PhotoImage(file="Images\\edureka.png")

Img_ico = Label(master, image=icon1)
Img_ico.place(x=0, y=0)
subject_lab = Label(master, text="Subject: ")
subject_lab.place(x=40, y=270)
To_lab = Label(master, text="To: ")
To_lab.place(x=40, y=230)
msg_lab = Label(master, text="Message: ")
msg_lab.place(x=40, y=310)


c2 = Entry(master)
c3 = Entry(master)
c4 = Entry(master)


c2.insert(30, "")
c3.insert(30, "")
c4.insert(100, "")


c2.place(x=120, y=270, height=25, width=220)
c3.place(x=120, y=230, height=25, width=220)
c4.place(x=120, y=310, height=25, width=420)


Button(master, text='START', width=15, height=2, bg='grey', fg = 'White', command=lambda: main_gui_connecter.main_gui_func(c2.get(), c3.get(), c4.get())).place(x=200, y=360, height=35, width=115)
Label(master, text ="For Support : Danish Ali WX854280    Contact : 00971508552942 ").place(x=70, y=410)
mainloop()