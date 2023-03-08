from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมนับแคลอรี่')
GUI.geometry('500x400')

L1 = Label(GUI,text='โปรแกรมนับแคลอรี่',font=('Angsana New',35),fg='red')
L1.place(x=30,y=20)
def Button2():
    text = '2,500 กิโลแคลอรี่'
    messagebox.showinfo('ปริมาณแคลอรี่เพิ่มขึ้น',text)

FB1 = Frame(GUI)
FB1.place(x=100,y=100)
B2 = ttk.Button(FB1,text='บริโภคอาหารเพิ่มขึ้นกี่แคล',command=Button2)
B2.pack(ipadx=20,ipady=20)

def Button3():
    text = '1,000 กิโลแคลอรี่'
    messagebox.showinfo('ปริมาณเเคลอรี่ลดลง.',text)

FB2 = Frame(GUI)
FB2.place(x=100,y=100)
B3 = ttk.Button(FB1,text='ออกกำลังกายลดลงไปกี่แคล',command=Button3)
B3.pack(ipadx=20,ipady=20)

GUI.mainloop()
