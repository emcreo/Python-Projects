##Python 3.7.3

#Author: Katherine Mazzolini
#Tested on Mac OS High Sierra v.10.13.6

from tkinter import *
import tkinter as tk

import check_files_gui


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.minsize(800,300)
        self.master.maxsize(800,300)
        self.master.title('Check Files')
        self.master.config(bg='lightgray')

        check_files_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    

