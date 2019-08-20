from tkinter import *
from tkinter import messagebox


class GUIFramework(Frame):
    """This is the GUI"""

    def __init__(self, master=None):
        """Initialize yourself"""

        """Initialise the base class"""
        Frame.__init__(self, master)

        """Set the Window Title"""
        self.master.title("RSS Reader - Eventually")
        top = self.winfo_toplevel()
        """Display the main window"
        with a little bit of padding"""
        self.grid(padx=15, pady=15, sticky=N + S + E + W)
        self.InitResizing()
        self.CreateWidgets()

    def InitResizing(self):
        """Initialize the Resizing of the Window"""
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(6, weight=1)

    def CreateWidgets(self):
        """Create all the widgests that we need"""

        """Create the Text"""
        self.lbRSSSiteText = Label(self, text="Select Site:")
        self.lbRSSSiteText.grid(row=0, column=0, sticky=W)
        self.lbRSSItemText = Label(self, text="Select RSS Item:")
        self.lbRSSItemText.grid(row=0, column=6, sticky=W)

        """Create the First ListBox"""
        scrollbarV = Scrollbar(self, orient=VERTICAL)
        scrollbarH = Scrollbar(self, orient=HORIZONTAL)

        self.lbSites = Listbox(self, selectmode=BROWSE
                               , yscrollcommand=scrollbarV.set
                               , xscrollcommand=scrollbarH.set
                               , relief=SUNKEN)
        self.lbSites.grid(row=1, column=0, columnspan=4, sticky=N + W + S + E)
        """Show the scrollbars and attatch them"""
        scrollbarV.grid(row=1, column=4, sticky=N + S)
        scrollbarV.config(command=self.lbSites.yview)
        scrollbarH.grid(row=2, column=0, columnspan=4, sticky=E + W)
        scrollbarH.config(command=self.lbSites.xview)
        """Set the command"""
        self.lbSites.bind("<Double-Button-1>", self.DblCLickSites)

        """Create the Add, Remove, Edit, and View Buttons"""
        self.btnAdd = Button(self, text="Add", command=self.Display)
        self.btnAdd.grid(column=0, row=3, stick=E, pady=5)
        self.btnRemove = Button(self, text="Remove", command=self.Display)
        self.btnRemove.grid(column=1, row=3, stick=E, pady=5)
        self.btnEdit = Button(self, text="Edit", command=self.Display)
        self.btnEdit.grid(column=2, row=3, stick=E, pady=5)
        self.btnView = Button(self, text="View", command=self.Display)
        self.btnView.grid(column=3, row=3, stick=E, pady=5)

        """Create a frame for space between the two items"""
        spaceframe = Frame(self, width=15)
        spaceframe.grid(row=3, column=5)

        """Create the Second ListBox"""
        scrollbarV = Scrollbar(self, orient=VERTICAL)
        scrollbarH = Scrollbar(self, orient=HORIZONTAL)

        self.lbRSSItems = Listbox(self, selectmode=BROWSE
                                  , yscrollcommand=scrollbarV.set
                                  , xscrollcommand=scrollbarH.set
                                  , relief=SUNKEN)
        self.lbRSSItems.grid(row=1, column=6, sticky=N + W + S + E)
        """Show the scrollbars and attatch them"""
        scrollbarV.grid(row=1, column=7, sticky=N + S)
        scrollbarV.config(command=self.lbRSSItems.yview)
        scrollbarH.grid(row=2, column=6, sticky=E + W)
        scrollbarH.config(command=self.lbRSSItems.xview)

        """Create the Frame for space between the ListBoxes and
        the Text"""
        spaceframe = Frame(self, height=5)
        spaceframe.grid(row=4, column=1)

        """Create the Text Widget"""
        scrollbarV = Scrollbar(self, orient=VERTICAL)
        scrollbarH = Scrollbar(self, orient=HORIZONTAL)
        self.txtItem = Text(self, wrap=WORD
                            , yscrollcommand=scrollbarV.set
                            , xscrollcommand=scrollbarH.set
                            , relief=SUNKEN
                            , takefocus=0
                            , borderwidth=1
                            , state=NORMAL
                            , cursor="arrow")
        self.txtItem.grid(row=5, column=0
                          , columnspan=7, sticky=N + W + S + E)
        """Show the scrollbars and attatch them"""
        scrollbarV.grid(row=5, column=7, sticky=N + S)
        scrollbarV.config(command=self.txtItem.yview)
        scrollbarH.grid(row=6, column=0, columnspan=7, sticky=E + W)
        scrollbarH.config(command=self.txtItem.xview)

        self.txtItem.tag_config("a", foreground="blue", underline=1)
        self.txtItem.tag_bind("a", "<Enter>", self.show_hand_cursor)
        self.txtItem.tag_bind("a", "<Leave>", self.show_arrow_cursor)
        self.txtItem.tag_bind("a", "<Button-1>", self.ClickText)
        self.txtItem.config(cursor="arrow")

        self.txtItem.insert(INSERT, "click here!", "a")
        self.txtItem.config(state=DISABLED)

        """Create the Set TextButton"""
        self.btnSetText = Button(self, text="SetText", command=self.SetStoryText)
        self.btnSetText.grid(column=6, row=3, stick=E, pady=5)

        """Just fill up the listbox with some numbers"""
        for i in range(40):
            self.lbSites.insert(END, i)
            self.lbRSSItems.insert(END, i)

    def show_hand_cursor(self, event):
        event.widget.configure(cursor="hand")

    def show_arrow_cursor(self, event):
        event.widget.configure(cursor="arrow")

    def DblCLickSites(self, event):
        """Called when lbSites is double-clicked on"
        event containts the x and y position of the click, but since
        we only care about the current selection we can ignore it"""
        self.Display()

    def ClickText(self, event):
        """Called when hypelink text is clicked on in the Text Widget
        event contians event information but since
        we only care about the current selection we can ignore it"""
        self.SetStoryText()

    def Display(self):
        """Called when btnDisplay is clicked, displays the contents of self.enText"""
        lstCurrSel = self.lbSites.curselection();
        strSelection = "";

        if (len(lstCurrSel) == 0):
            strSelection = "Nothing yet!"
        else:
            strSelection = self.lbSites.get(lstCurrSel)
        tkMessageBox.showinfo("Text", "You selected: %s" % strSelection)

    def SetStoryText(self):
        """Set the Story text, called form the btnSetText"""

        """Get the Current selection"""
        lstCurrSel = self.lbRSSItems.curselection();
        strSelection = "";

        if (len(lstCurrSel) == 0):
            strSelection = "Nothing yet!"
        else:
            strSelection = self.lbRSSItems.get(lstCurrSel)
        """Set the Text Widgets text"""
        self.txtItem.config(state=NORMAL)
        self.txtItem.delete(1.0, END)
        self.txtItem.insert(INSERT, strSelection, "a")
        self.txtItem.config(state=DISABLED)


if __name__ == "__main__":
    guiFrame = GUIFramework()
    guiFrame.mainloop()