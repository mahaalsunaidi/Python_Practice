import tkinter
from tkinter import *



class GUI:
    def addfun(self):
        # Adding names to the left window
        if (self.text.get() != ""):
            self.reaultOfMassege = "Successfully Added!"
            self.result = self.text.get()
            self.label1.configure(text=self.reaultOfMassege)
            self.Box1.insert(0, self.result)
            self.text.delete(0, 9999999)

    def deletefun(self):
        # Delete selected name
        if (self.Box1.size() != 0 and self.Box1.curselection() != ()):
            self.position = self.Box1.curselection()
            self.reaultOfMassege = "Selected name was deleted!"
            self.result = self.Box1.get(self.position)
            self.label1.configure(text=self.reaultOfMassege)
            self.Box1.delete(0, self.position)

    def moveRight(self):
        # move selected name to the right window
        if (self.Box1.size() != 0 and self.Box1.curselection() != ()):
            self.position = self.Box1.curselection()
            self.result = self.Box1.get(self.position)
            self.Box2.insert(0, self.result)
            self.Box1.delete(0, self.position)

    def moveAllR(self):
        # move all names on the left to the right window
        self.listSize = self.Box1.size()
        for line in range(self.listSize):
            self.result = self.Box1.get(line)
            self.Box2.insert(END, self.result)
        self.Box1.delete(0, self.listSize)

    def moveLeft(self):
        # move selected names to the left window
        if (self.Box2.size() != 0 and self.Box2.curselection() != ()):
            self.position = self.Box2.curselection()
            self.result = self.Box2.get(self.position)
            self.Box1.insert(0, self.result)
            self.Box2.delete(0, self.position)

    def moveAllL(self):
        # move all names to the left window
        self.listSize = self.Box2.size()
        for line in range(self.listSize):
            self.result = self.Box2.get(line)
            self.Box1.insert(END, self.result)
        self.Box2.delete(0, self.listSize)

    def __init__(self, root):
        self.root = root
        self.label1 = tkinter.Label(root, text="  ", highlightbackground="light blue", highlightcolor="light blue",
                                    highlightthickness=1, bd=0)
        self.label1.grid(column=3, row=0, pady=5)

        self.text = Entry(root, width=20, state='normal', highlightbackground="light blue", highlightcolor="light blue",
                          highlightthickness=1, bd=0)
        self.text.grid(column=0, row=0, pady=5, padx=5)
        self.text.focus()

        self.scoreForFrame1 = LabelFrame(root, relief=FLAT)
        self.scoreForFrame1.grid(column=0, columnspan=2, padx=10)

        self.scrollbar = tkinter.Scrollbar(self.scoreForFrame1)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.Window1 = Listbox(self.scoreForFrame1, height=8, yscrollcommand=self.scrollbar.set,
                            highlightbackground="light blue",
                            highlightcolor="light blue", highlightthickness=1, bd=0)
        self.Window1.pack()

        self.scrollbar.config(command=self.Window1.yview)

        self.labelForFrame = LabelFrame(root, relief=FLAT)
        self.labelForFrame.grid(column=1, row=1, columnspan=2)

        self.rightBotton = tkinter.Button(root, text=">", command=self.moveRight)
        self.rightBotton.grid(in_=self.labelForFrame, row=0)

        self.AllToRight = tkinter.Button(root, text=">>", command=self.moveAllR)
        self.AllToRight.grid(in_=self.labelForFrame, row=1, pady=5)

        self.leftBotton = tkinter.Button(root, text="<", command=self.moveLeft)
        self.leftBotton.grid(in_=self.labelForFrame, row=2, pady=5)

        self.AllToLeft = tkinter.Button(root, text="<<", command=self.moveAllL)
        self.AllToLeft.grid(in_=self.labelForFrame, row=3)

        self.scrolForFrame2 = LabelFrame(root, relief=FLAT)
        self.scrolForFrame2.grid(column=3, row=1)

        self.scrollbar2 = tkinter.Scrollbar(self.scrolForFrame2)
        self.scrollbar2.pack(side=RIGHT, fill=Y)

        self.Window2 = Listbox(self.scrolForFrame2, height=8, yscrollcommand=self.scrollbar2.set,
                            highlightbackground="light blue",
                            highlightcolor="light blue", highlightthickness=1, bd=0)
        self.Window2.pack()

        self.scrollbar.config(command=self.Window2.yview)

        self.addBouton = tkinter.Button(root, text="Add", command=self.addfun)
        self.addBouton.grid(column=2, row=0, pady=5, padx=5)

        self.deleteBotun = tkinter.Button(root, text="Delete", command=self.deletefun)
        self.deleteBotun.grid(column=0, row=6, columnspan=2, pady=5)


if __name__ == '__main__':
    root = Tk()
    gui = GUI(root)
    root.title('')
    root.geometry('400x205')
    root.mainloop()
