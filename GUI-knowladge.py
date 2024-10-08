from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()  
GUI.title('save data')
GUI.geometry('500x400')

B1 = ttk.Button(GUI,text='your monry')
B1.pack(ipadx=20,ipady=20)
B1.place(x=20,y=80)
def Button2():
    text = 'now i have 300 bath'
    messagebox.showinfo('my money',text)


FB1 = Frame(GUI)
FB1.place(x=100,y=300)
B2 = Button(FB1,text='your mouth',command=Button2)
B2.pack(ipadx=20,ipady=20)

L1 = Label(GUI,text='my classroom',font=('Angsana New',30),fg='blue')
L1.place(x=30,y=20)
GUI.mainloop()
