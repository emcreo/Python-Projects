##Python 3.7.3
#
#
#Author: Katherine Mazzolini
#Tested on Mac OS High Sierra v.10.13.6

from tkinter import *
import tkinter as tk

import check_files_main


def load_gui(self):
        
    self.btnBrowse1 = tk.Button(self.master, width=14, height=2, text='Browse...', font=('helvetica', 16), fg='black', bg='lightgray', command=lambda: check_files_func.browse1(self))
    self.btnBrowse1.grid(row=1, column=0, padx=(25,0), pady=(45,0), sticky=W)
    
    self.btnBrowse2 = tk.Button(self.master, width=14, height=2, text='Browse...', font=('helvetica', 16), fg='black', bg='lightgray', command=lambda: check_files_func.browse2(self))
    self.btnBrowse2.grid(row=2, column=0, padx=(25,0), pady=(45,0), sticky=W)
    
    self.btnFileCheck = tk.Button(self.master, width=14, height=3, text='Check for files...', font=('helvetica', 16), fg='black', bg='lightgray', command=lambda: check_files_func.fileCheck(self))
    self.btnFileCheck.grid(row=3, column=0, padx=(25,0), pady=(45,0), sticky=S+W)
    
    self.btnClose = tk.Button(self.master, width=14, height=2, text='Close', font=('helvetica', 20), fg='black',bg='lightgray',command=lambda: check_files_func.close(self))
    self.btnClose.grid(row=3, column=1, columnspan=3, padx=(450,10), pady=(45,0), sticky=E+S)

    self.txt_Browse1 = tk.Entry(self.master, text='', font=('helvetica', 16), width=44) 
    self.txt_Browse1.grid(row=1, column=1, columnspan=4, padx=(100,10), pady=(45,0), sticky=E+W)

    self.txt_Browse2 = tk.Entry(self.master, text='', font=('helvetica', 16), width=44)  
    self.txt_Browse2.grid(row=2, column=1, columnspan=4, padx=(100,10), pady=(45,0), sticky=E+W)

if __name__ == "__main__":
    pass





