from tkinter import *
import time
import datetime
root = Tk()

#theLabel = Label (root, text = "First GUI Program")
#theLabel.pack()

"""topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

redButton = Button (topFrame, text = "Red", fg = "red")
redButton.pack(side = LEFT)

blueButton = Button (topFrame, text = "Blue", fg = "light Blue")
blueButton.pack(side = LEFT)

yellowButton = Button (topFrame, text = "Yellow", fg = "light yellow")
yellowButton.pack(side = LEFT)

greenButton = Button (bottomFrame, text = "Green", fg = "light green")
greenButton.pack(side = BOTTOM)"""
t = datetime.datetime.now()

print(t.isocalendar()[1])
print("Week day", datetime.datetime.today().weekday())

label1 = Label(root, text="Name")
label2 = Label(root, text="Password")

label1.grid(row=0)
label2.grid(row=1)

entry1 = Entry(root)
entry2= Entry(root)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

root.mainloop()