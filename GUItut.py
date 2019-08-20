import tkinter
from tkinter import *

root = Tk()
#theLabel = Label(root, text="Hey this is GUI by Python")
#theLabel.pack()

"""topFrame = Frame(root)
topFrame.pack(side = TOP)

bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

button1 = Button(topFrame, text="Button-1", fg="light blue")
button1.pack(side=LEFT, expand=YES, fill=X)"""
root.geometry("500x500")

can = tkinter.Canvas(root, width=200, height=450, bg ="lightyellow")
lab = Label(root, text = "تكفون بتخرج", bg="lightblue")
lab.place(x=30, y = 50)
b = 1
"""for e in range(6):
    lab2 = Label(root, text = e+1, bg="lightblue")
    lab2.place(x=65, y=80+(20 *e))
    b=b +1
"""
img = tkinter.PhotoImage(file="PSUDefaultRollUp.png")
a = Label(root,image = img)
a.place(x=0,y=280)

img1 = tkinter.PhotoImage(file ="images.png")
b = Label(root, image =img1)
b.place(x = 200, y = 30)
#ov = Canvas.create_oval(100, 120, 50, fill="blue", outline="#DDD", width=4)
can.pack(side=LEFT)




root.mainloop()