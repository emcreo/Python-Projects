#Python 3.7.3
#
#Author: Katherine
#Tested on Mac OS High Sierra v.10.13.6

from tkinter import*
import tkinter as tk
import search_main
import search_func



def load_gui(self):


    
    self.btnSearch = tk.Button(self.master, width=14, height=2, text='Search', font=('helvetica', 16), fg='black', command=lambda: search_func.askdir(self))
    self.btnSearch.grid(row=1, column=0, padx=(25,0), pady=(45,0), sticky=NW)

    self.txtSearch = tk.Entry(self.master, text='', textvariable=self.src_entry, font=('helvetica', 16), width=44)
    self.txtSearch.grid(row=1, column=1, columnspan=4, padx=(15,0), pady=(45,0), sticky=W)

    



if __name__ == "__main__":
    pass
