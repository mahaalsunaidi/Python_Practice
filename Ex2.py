import tkinter
from tkinter import *
master = tkinter.Tk()

root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.pack()

canvas_width = 190
canvas_height =150



w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

w.create_oval(50,50,100,100)

buttonblue = tkinter.Button(frame, text="Blue",  fg="blue", command=)
buttonblue.pack (side = LEFT)

buttonred = tkinter.Button(frame, text="Red",  fg="red", command= )
buttonblue.pack (side = LEFT)

buttonyellow = tkinter.Button(frame, text="Yellow",  fg="yellow", command= )
buttonblue.pack (side = LEFT)


def oddblue(a,b,c):
    if len(myvar.get())%2 == 0:
        mywidget.config(bg='red')
    else:
        mywidget.config(bg='lightblue')
    mywidget.update_idletasks()
    root = tkinter.Tk()
myvar = StringVar()
myvar.set('')
mywidget = tkinter.Entry(root, textvariable=myvar, width=10)
mywidget.pack()
mywidget.focus()
myvar.trace('w',oddblue)


mainloop()


