import tkinter
from tkinter import *


root = tkinter.Tk()

LFrame = Frame(root)
LFrame.pack(side=LEFT)

label = Label(LFrame, text="instruction")
label.pack()


for n in range(1, 11):
    inst = Label(LFrame, text=n)
    inst.pack()

img = PhotoImage(file="PSUDefaultRollUp.png")
Label(LFrame, image=img).pack()

Rframe = Frame(root)
Rframe.pack(side=RIGHT)

canvas = Canvas(Rframe)
oval = canvas.create_oval(25, 25, 200, 200, fill="white", outline="")
canvas.pack()

def white():
    oval = canvas.create_oval(25, 25, 200, 200, fill="white")
    canvas.pack()

def printRed():
    colorLog.insert(END,'Red \n')
    oval = canvas.create_oval(25, 25, 200, 200, fill="red", outline="")
    canvas.pack()


def printYellow():
    colorLog.insert(END, 'Yellow \n')
    oval = canvas.create_oval(25, 25, 200, 200, fill="yellow", outline="")
    canvas.pack()


def printGreen():
    colorLog.insert(END, 'Green \n')
    oval = canvas.create_oval(25, 25, 200, 200, fill="green", outline="")
    canvas.pack()


button = tkinter.Button(Rframe, text="Red", command=printRed, fg="red")
button.pack(side = LEFT)

button2 = tkinter.Button(Rframe, text="Yellow", command=printYellow, fg="yellow")
button2.pack(side=LEFT)

button3 = tkinter.Button(Rframe, text="Green", command=printGreen, fg="green")
button3.pack(side=LEFT)

colorLog = tkinter.Text(Rframe, width=30, height=10, takefocus=0)
#colorLog.bind(button, white())
colorLog.pack(side=BOTTOM, fill="none")




mainloop()


