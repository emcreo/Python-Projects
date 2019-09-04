##Python 3.7.3
#Author: Katherine Mazzolini
#Tested on Mac OS High Sierra v.10.13.6

from tkinter import *
import tkinter as tk
import os
import shutil
import ta_123_main
import ta_123V2_func

def load_gui(self):

    self.btn_src = tk.Button(self.master, width=18, height=2, text='Choose Source...', font=('helvetica', 16), fg='black', bg='lightgray', command=lambda: ta_123V2_func.btn_src(self)) 
    self.btn_src.grid(row=1, column=0, padx=(25,0), pady=(45,0), sticky=W)

    self.btn_dest = tk.Button(self.master, width=18, height=2, text='Choose Destination...', font=('helvetica', 16), fg='black', bg='lightgray', command=lambda: ta_123V2_func.btn_dest(self)) 
    self.btn_dest.grid(row=2, column=0, padx=(25,0), pady=(45,0), sticky=W)

    self.btn_exec = tk.Button(self.master, width=16, height=2, text='Execute', font=('helvetica', 16), fg='black', bg='lightgray', command=lambda: ta_123V2_func.btn_exec(self))
    self.btn_exec.grid(row=3, column=4, padx=(25,60), pady=(45,0), sticky=S+W)

    self.txtBrowse1 = tk.Entry(self.master, width=40, textvariable=self.browse1, text='', font=('helvetica', 16))
    self.txtBrowse1.grid(row=1, column=1, columnspan=4, padx=(100,10), pady=(45,0), sticky=E+W)

    self.txtBrowse2 = tk.Entry(self.master, width=40, textvariable=self.browse2, text='', font=('helvetica', 16))
    self.txtBrowse2.grid(row=2, column=1, columnspan=4, padx=(100,10), pady=(45,0), sticky=E+W)

if __name__ == "__main__":
    pass

    
