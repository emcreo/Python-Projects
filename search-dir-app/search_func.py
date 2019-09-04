#Python 3.7.3
#
#Author: Katherine
#Tested on Mac OS High Sierra v.10.13.6

import os
from tkinter import filedialog
from tkinter.filedialog import askdirectory 
from tkinter import *
import tkinter as tk


import search_main
import search_gui

        


def askdir(self):
    dirname = askdirectory()
    self.src_entry.set(dirname)
    print (self.txtSearch.insert(INSERT,dirname))
            



if __name__ == "__main__":
    pass
