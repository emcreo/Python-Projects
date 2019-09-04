#Python 3.7.3
#Author: Katherine Mazzolini
#Tested on Mac OS High Sierra 10.13.6

from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askdirectory
import os
import shutil
import sqlite3
import ta_123_main
import ta_123_gui
import time

def create_db_123():
    conn = sqlite3.connect('db_123.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT, col_file TEXT)")
        conn.commit()
    conn.close()

    
def first_run(self):
    conn = sqlite3.connect('dB_123.db')
    with conn:
        cur = conn.cursor()

        cur.executemany("INSERT INTO tbl_files(col_file) VALUES (?)", ('hello1.py'))
        cur.executemany("INSERT INTO tbl_files(col_file) VALUES (?)", ('hello2.py'))
        cur.executemany("INSERT INTO tbl_files(col_file) VALUES (?)", ('hello3.py'))
        cur.executemany("INSERT INTO tbl_files(col_file) VALUES (?)", ('python1.rtf'))
        cur.executemany("INSERT INTO tbl_files(col_file) VALUES (?)", ('python2.rtf'))
        cur.executemany("INSERT INTO tbl_files(col_file) VALUES (?)", ('python3.rtf'))
        cur.executemany("INSERT INTO tbl_files(col_file) VALUES (?)", ('python4.rtf'))
        cur.executemany("INSERT INTO tbl_files(col_file) VALUES (?)", ('python5.rtf'))
        cur.executemany("INSERT INTO tbl_files(col_file) VALUES (?)", ('python.pages'))
        cur.executemany("INSERT INTO tbl_files(col_file) VALUES (?)", ('python-test.numbers'))
        conn.commit()
    conn.close()
    

def btn_exec(self):
    conn = sqlite3.connect('dB_123.db')
    with conn:
        cur = conn.cursor()
        
        src = self.browse1.get()
        print(src)
        i = 0
        for i in os.listdir(src):
            dest = self.browse2.get()
            if i.endswith('.rtf'):
                cur.execute("INSERT INTO tbl_files(col_file) VALUES (?)", (i,))
                stamp = os.path.join(src,i)
                print(time.ctime(os.path.getmtime(stamp)))
                shutil.move(stamp,dest)
                
        conn.commit()
    conn.close()
"""             
def btn_exec(self):
    src = self.browse1.get()
    i = 0
    for i in os.listdir(src):
        dest = self.browse2.set(i)
        if i.endswith(".rtf"):
            stamp = os.path.join(src,i)
            shutil.move(stamp,dest)
            print(i.os.path.getmtime(stamp))
"""

def btn_src(self):
    dirname = askdirectory()
    self.browse1.set(dirname)
    self.txtBrowse1.insert(INSERT,dirname)
        
def btn_dest(self):
    dirname = askdirectory()
    self.browse2.set(dirname)
    self.txtBrowse2.insert(INSERT,dirname)



if __name__ == "__main__":
    #create_db_123(self)
    pass
