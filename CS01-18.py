from tkinter import *
root = Tk()
root.title("First GUI")
MyText = Label(text="My name is ",fg="Blue",font=20).grid(row=0,column=0)
MyText = Label(text="Thanatip ",fg="Green",font=20).grid(row=1,column=1)
MyText = Label(text="Khongchob ",fg="Red",font=20).grid(row=2,column=2)
root.geometry("300x300")
root.mainloop()