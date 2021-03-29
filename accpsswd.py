"""
accpsswd = account & password.

This is a program to store usernames and psswds 
for different platforms and accounts

The user can:
search, add, update, delete
any e4 from the database

"""

#importing reqd:

from tkinter import *
from tkinter import ttk
try:    
    import tkinter as tk    #to work in both python 2 or in python 3
except ImportError:
    import Tkinter as tk
import backend as bck #importing the backend.py file to utilise the functions.
import datetime

#<<<<<<<<<<<<<  functions for linking buttons :   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#note the functions should be made before calling them in the buttons using command
#for viewall button to insert all entries into listbox:
def listbox_insert(): 
    lb.delete(0,END)
    for entry in bck.view():
        lb.insert(END,entry)

def searcher():
    lb.delete(0,END)
    for entry in bck.search(account_text.get(),name_text.get(),userid_text.get(),note_text.get()):
        lb.insert(END,entry)

def adder():
    bck.add(account_text.get(),name_text.get(),userid_text.get(),password_text.get(),note_text.get(),date_text.get())
    lb.delete(0,END)
    lb.insert(END,'account : '+account_text.get(),'name : '+name_text.get(),'userid : '+userid_text.get(),'password : '+password_text.get(),'note : '+note_text.get(),'date : '+date_text.get())
    

def clearer():
    bck.clear_all()
    lb.delete(0,END)
    lb.insert(0,' ALL ENTRIES HAVE BEEN CLEARED :) ')

def get_selected_row(event):
    global selected_entry   #to use the selected enrty variable outside the function...
    index = lb.curselection()[0]
    selected_entry = lb.get(index)
    return(selected_entry) 

def deleter():
    bck.remove(selected_entry[0])
    lb.delete(0,END) #to refersh the page.
    for entry in bck.view():
        lb.insert(END,entry)

#for update button:
def updater():
    bck.update(account_text.get(),name_text.get(),userid_text.get(),password_text.get(),note_text.get(),date_text.get(),selected_entry[0])
    lb.delete(0,END)
    lb.insert(END,'ACCOUNT SUCCESSFULLY UPDATED'+'account : '+account_text.get(),'name : '+name_text.get(),'userid : '+userid_text.get(),'password : '+password_text.get(),'note : '+note_text.get(),'date : '+date_text.get())
    




#adding differnt components of the frontend tkinter window:
if __name__ == '__main__':
    window = tk.Tk() #mainwindow
    window.geometry('735x300') # bxl
    window.title('haccpswd')

#labels:


l1 = Label(window,text='Account')
l1.grid(row='0',column='0')
l1.config(font=("Arial", 11))
l2 = Label(window,text='Name')
l2.grid(row='1',column='0')
l2.config(font=("Arial", 11))
l3 = Label(window,text='User Id')
l3.grid(row='2',column='0')
l3.config(font=("Arial", 11))
l4 = Label(window,text='Password')
l4.grid(row='3',column='0')
l4.config(font=("Arial", 11))
l5 = Label(window,text='Date')
l5.grid(row='5',column='0')
l5.config(font=("Arial", 11))
l6 = Label(window,text='Notes')
l6.grid(row='6',column='0')
l6.config(font=("Arial", 11))

#entries:
#account
account_text =StringVar()
e1 = Entry(window,textvariable=account_text)
e1.grid(row='0',column='1')
e1.config(font=("Courier", 12))
#name
name_text=StringVar()
e2 = Entry(window,textvariable=name_text)
e2.grid(row='1',column='1')
e2.config(font=("Courier", 12))
#userid
userid_text=StringVar()
e3 = Entry(window,textvariable=userid_text)
e3.grid(row='2',column='1')
e3.config(font=("Courier", 12))
#password & for psswd veiwing checkbox:
password_text=StringVar()
def toggle_password():
    global e4, checkbutton
    if checkbutton.var.get():
        e4['show'] = "\uE335" #emoji uni-code	
    else:
        e4['show'] = ""
    #checkbox for password:
checkbutton = tk.Checkbutton(window,text="Hide password",onvalue=True,offvalue=False,command=toggle_password)                                                                                  
e4 = tk.Entry(window,textvariable=password_text)
e4.default_show_val = e4['show']
e4['show'] = "\uE335" #to show emoji:
checkbutton.var = tk.BooleanVar(value=True) #
checkbutton['variable'] = checkbutton.var
e4.grid(row='3',column='1')
e4.config(font=("Courier", 12))
checkbutton.grid(row=4,column=1)

#date text show
today_date = datetime.date.today()#to convert into dd mm yyyy
new_today_date = today_date.strftime("%d/%m/%Y")
print (new_today_date)        
date_data = str(new_today_date)
today_date = datetime.date.today()#to convert into dd mm yyyy
new_today_date = today_date.strftime("%d/%m/%Y")
print (new_today_date)        
date_data = str(new_today_date)
date_text = StringVar()
e5 = Entry(window,textvariable=date_text)
e5.insert(END,date_data)
e5.grid(row='5',column='1')
e5.config(font=("Courier", 12))

#note
note_text=StringVar()
e6 = Entry(window,textvariable=note_text)
e6.grid(row='6',column='1')
e6.config(font=("Courier", 12))

#list box with scrollbar:
lb = Listbox(window,height=10,width=60,bg='yellow')
lb.grid(row=0,column=2,rowspan=7,columnspan=1)
scroll = Scrollbar(window)
lb.configure(yscrollcommand=scroll.set)
scroll.grid(row=0,column=5,rowspan=7,columnspan=1)
scroll.configure(command=lb.yview)
lb.bind('<<ListboxSelect>>',get_selected_row)           #to select row on listbox:


#buttons:
b1 = Button(window,text='View all',height=2,width=17,padx='2.5',pady='2.5',command=listbox_insert)
b1.grid(row=9,column=1)
b1.config(font=("Arial", 14))
b2 = Button(window,text='Add entry',height=2,width=12,bg='green',padx='2.5',pady='2.5',command=adder)
b2.grid(row=8,column=0)
b2.config(font=("Arial", 14))
b3 = Button(window,text='Remove entry',height=2,width=12,bg='red',padx='2.5',pady='2.5',command=deleter)
b3.grid(row=9,column=0)
b3.config(font=("Arial", 14))
b4 = Button(window,bg='orange',text='Update entry',height=2,width=12,padx='2.5',pady='2.5',command=updater)
b4.grid(row=8,column=2,sticky='WE')
b4.config(font=("Arial", 14))
b5 = Button(window,text='Search',height=2,width=17,padx='2.5',pady='2.5',command=searcher)
b5.grid(row=8,column=1)
b5.config(font=("Arial", 14))
b6 = Button(window,text='Close',height=2,width=20,padx='2.5',pady='2.5',command=window.destroy)
b6.grid(row=9,column=2,sticky='W')
b6.config(font=("Arial", 14))

#special clear all entry popup confirmer:
def clear_confirmer():
    win = tk.Toplevel()
    win.title("deleter")
    win.geometry('250x75')
    l = tk.Label(win, text="All entries will be deleted !!")
    l.config(font=("Arial", 14))
    l.grid(row=0, column=0)
    byes = ttk.Button(win, text="Okay", command=clearer)
    byes.grid(row=1, column=0,sticky='E')
    bno = ttk.Button(win, text="NOOO",command=win.destroy)
    bno.grid(row=1, column=0,sticky='W')

b7 = Button(window,text='CLEAR ALL',bg='purple',height=2,width=8,padx='2.5',pady='2.5',command=clear_confirmer)
b7.grid(row=9,column=2,sticky='ES')
b7.config(font=("Arial", 8))




















window.mainloop() #lastline for closing
