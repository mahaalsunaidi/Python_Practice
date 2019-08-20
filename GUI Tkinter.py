from tkinter import *


def clicked():
    res = "Welcome " + txt.get()
    label.configure(text=res)


root = Tk()
root.geometry("250x250")
root.title("First GUI")

TopFrame = Frame(root)
TopFrame.pack(side=TOP)

RightFrame = Frame(root)
RightFrame.pack(side=RIGHT)

LeftFrame = Frame(root)
TopFrame.pack(side=LEFT)

BottomFrame = Frame(root)
BottomFrame.pack(side=BOTTOM)

label = Label(TopFrame, text="Testing Labels")
label.grid(column=0, row=0)
label.pack()

label1 = Label(BottomFrame, text="Fonts", font=("Arial", 25))
label1.pack()

txt = Entry(RightFrame,width=10)
txt.pack()

btn = Button(RightFrame, text="Click", fg="blue", command=clicked)
btn.grid(row=0, column=0, sticky=W)
btn.pack()






root.mainloop()

