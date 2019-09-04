import os
from tkinter import *
import tkinter as tk
import sqlite3

import phonebook_main
import phonebook_gui

def center_window(self,w,h): #passing in tkinter frame (master) reference and
    #the w & h to get user's screen w & h  (this is for Windows only, not for Mac)
    screen_width = self.master.winfo_screenwidth()#self.master is primary window, so we are
    #accessing the user's width & height with winfo which is a tk method
    #to do calculations
    screen_height = self.master.winfo_screenheight()
    #calculate x & y coordinates to paint the app centered on user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo
#center_window can be deleted if needed


#catch if the user clicks on the windows upper-right 'X' to ensure they want to close
#tkinter class messagebox has a method canned asktocancel
def ask_quit(self):
    if messagebox.askokcancel('Exit program', "Okay to exit application?"):
        self.master.destroy()#this closes app
        os._exit(0)#takes all the wigits and fully deletes from memory
        #os module defined method

#=============================================================================
def create_db(self):
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fnames TEXT, \
            col_lnames TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            );")
        #must commit() to save changes & close dB connection
        conn.commit()
    conn.close()
    first_run(self)


def first_run(self):
    data = ('John', 'Doe', 'John Doe','111-111-1111','jdoe@gmail.com')
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""", (data))
            conn.commit()
    conn.close()

                        
def count_records(cur): #passing in the sqlite3 cursor for permission to use it
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
    count = cur.fetchone()[0]#call the first index of the tuple above
    return cur,count

#select item in ListBox
def onSelect(self,event):
    #calling the event is the self.lstList1 widgit
    varList = event.widgit
    select = varList.curselection()[0]
    value = varList.get(select)#to get the text name of whatever that's coordinated to the index number
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email) FROM tbl_phonebook WHERE col_fulname = (?)""", [value])
        varBody = cursor.fetchall()
        #this returns a tuple and we can slice it into 4 parts using data[] during the iteration
        for data in varBody:
            self.txt_fname.delete(0,END)#deleted anything in the text box
            self.txt_fname.insert(0,data[0])#add to textbox
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])

def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    #normalize the data to keep it consistent in the database
    var_fname = self.txt_fname.strip() #removes any blank space before & after the user's entry
    var_lname = self.txt_fname.strip() #ensures first character in eac word is capitalized
    var_fname = self.txt_fname.title()#create a capital letter in the name
    var_lname = self.txt_fname.title()
    var_fullname = ('{} {}'.format(var_fname,var_lname)) #combines normalized names into a fullname
    print('var_fullname: {}'.format(var_fullname)) # for development
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    #if not "@" or not "." in var_email: #will use this soon
       # print("Incorrect email format!!")
    if (len(var_fname)) > 0 and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0): #enforce user to provide both names
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cursor = conn.coursor()
            #check dB for existance of fullname, if so alert user and disregard request
            cursor.excute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col-fullname = '{}'""".format(var_fullname))#,(var_fullname)
            count = cursor.fetchone()[0]
            chkNmae = count
            if chkName == 0: #if this is 0 then there is not existance of the full name & we can add new data
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_phonebook(col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""",var_fname,var_lname,var_phone,var_email)
                self.lstList1.insert(END, var_fullname) #update listbox with the new fullname
                onClear(self) #call the function to clear all of the textboxxes
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all four fields.")

def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection()) #listbox's selected value
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        #check count to sensure this is not the last record in
        #the database...cannot delet last record or we will get an error
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permentantly deleted from the database. \n\nProceed with the deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('phonebook.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELET FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self) #call the function to clear all of the textboxes and the selected index of listbox
#####               onRefrest(self) #update the listbox of the changes
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error","({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).".fomat(var_select))
    conn.close()

def onDeleted(self):
    #clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
##      onRefresh(self) #update the listbox of the changes
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass
def onClear(self):
    #clear the text in these texboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)

def onRefresh(self):
    #populate the listbox, coinciding with the database
    self.lstList1.delete(0,End)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_phonebook""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.inser(0,str(item))
                i = i + 1
    conn.close()

def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0] #index of the list selction
        var_value = self.lstList1.get(var_select) #list selection's text value
    except:
        messagebox.showinfo("Missing selection","No name was selected from the list box. \nCancelling the Update request.")
        return
    #the user will only be allowed to update changes for phone and emails.
    #for name changes the user will need to delet the entire record and start over
    var_phone = self.txt_phone.get().strip() #normalize the data to maintain databse integrity
    var_email = self.txt_email.get().strip()
    if(len(var_phone) > 0) and (len(var_email) > 0): #ensure there is data present
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cur = conn.cursor()
            #count records to see if the user's changes are already in the database...meaning, there are no changes to update
            cur.execute("""SELECT COUNT(col_phone) FROM tbl-phonebook WHERE col_phone = '{}'""".format(var_phone))
            count = cur.fetchone()[0]
            print(count)
            cur.execute("""SELECT COUNT(col_email) FROM tbl-phonebook WHERE col_email = '{}'""".format(var_email))
            count2 = cur.fetchone()[0]
            print(count2)
            if count == 0 or count2 == 0: #if proposed changes are not already in database, then proceed
                response = messagebox.askokcancel("Udate Request","The following changes ({}) and ({}) will be implemented for ({}.\n\nProceed with the update request?".format(var_phone,var_email))
                print(response)
                if response:
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_phonebook SET col_phone = '(0)',col_email = '(1)' WHERE col_fullname = '(2)'""".format(var_phone,var_email,var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request","No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected.","Both ({}) and ({}) \nalready exist in the database for this name. \n\nYour update has been cancelled.".format(var_phone,var_email))
            onClear(self)
        conn.close()
    else:
        messagebox.showerror("Missing information","Please select a name from the list. \nThen edit the phone or email information.")
    onClear(self)


if __name__=="__main__":
    pass

    
            




            
            
    
            
    
        


    


            
            
        
                    
            















    
