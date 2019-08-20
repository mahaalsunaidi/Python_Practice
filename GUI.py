import tkinter
from tkinter import *

root = Tk()
Label(root,text="Shit", bg= "blue", ).pack(fill = X)
Label(root, text="This is thing is so much stressful and it's the worst thing ever", fg ="white", bg = "black").pack()


mainloop()

'''class MyFirstGUI:
    def __init__ (self, master):
        self.master = master
        master.title("A simple GUI")
        self.initialize(master)

    def initialize(self,master):
        self.label = tkinter.Label(master, text = "This is our first GUI")
        self.label.pack()
        self.greet_button = tkinter.Button(master, text = "Greet", command = self.greet)
        self.greet_button.pack()
        self.close_button = tkinter.Button(master, text = "Close", command = master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

if __name__ == '__main__':
    root = tkinter.Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()

import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, height=42, width=42)
        self.entry = tk.Entry(self)
        self.entry.focus()
        self.entry.pack()
        self.clear_button = tk.Button(self, text="Clear text", command=self.clear_text)
        self.clear_button.pack()

    def clear_text(self):
        self.entry.delete(0, 'end')

def main():
    root = tk.Tk()
    App(root).pack(expand=True, fill='both')
    root.mainloop()

if __name__ == "__main__":
    main()'''
