#Python 3.7.3
#
#Author: Katherine
#Tested on Mac OS High Sierra v.10.13.6


from tkinter import *
import tkinter as tk
import search_gui
import search_func



class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.minsize(600, 200)
        self.master.maxsize(600, 200)
        self.master.title('Search File System')
        self.master.config(bg='lightblue')
        self.src_entry = StringVar()
        search_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


