#Python 3.7.3
#Author: Katherine Mazzolini
#Tested on Mac OS High Sierra 10.13.6

from tkinter import *
import tkinter as tk
import os
import shutil
import ta_123_gui
import ta_123V2_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.minsize(700,300)
        self.master.maxsize(700,300)
        self.master.title('TA Drill 123')
        self.master.config(bg='lightgray')
        self.browse1 = StringVar()
        self.browse2 = StringVar()

        
        ta_123_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
