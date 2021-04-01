
# This file displays the signup screen
from tkinter import *
import tkinter as tk
from tkinter import scrolledtext as st
import top_level_backend as tlb

#database function and functions to get the strvars:
def adder():
    tlb.add(name.get(),global_user_name.get(),global_password.get(),email.get())
    print("in add")
    # lb.delete(0,END)
    # lb.insert(END,'account : '+account_text.get(),'name : '+name_text.get(),'userid : '+userid_text.get(),'password : '+password_text.get(),'note : '+note_text.get(),'date : '+date_text.get())

def showSignature():
    text = 'Group09\n\t  \n\n\tMembers: \n\t Hamzah Khalid Baig   [19CO20] \n\t Uzair Shahid Kazi    [19CO22] \n\t Aaftab Harun khan    [19CO23] \n\t Mohammad Ziya-ul-Haq [19CO37]'
    return text

def about(*event):
    global aboutWindow
    aboutWindow = Tk()
    aboutWindow.geometry("300x200")
    aboutWindow.resizable(0,0)

    aboutText = showSignature()

    paper = st.ScrolledText(aboutWindow, width=350, height=200, font=("Consolas", 11))
    paper.insert("1.0", aboutText)
    paper.configure(state='normal')
    paper.pack()

    aboutWindow.mainloop()

#This function destroys the main window
def exitWindow(*event):
    roots.destroy()
def signin(*event):
    roots.destroy()
    global signinwindow # These globals just make the variables global to the entire script, meaning any definition can use them.
    signinwindow = Tk() # This creates the window, just a blank one.
    signinwindow.title('Password Management System') # This renames the title of said window to 'signup'
    signinwindow.geometry('700x300')
    signinwindow.resizable(0,0)
#instruction
    instruction = Label(signinwindow, text='Please Enter Credentials to login',justify='center',  font="Helvetica 20 bold", bg="skyblue") # This puts a label, so just a piece of text saying 'please enter blah5
    instruction.grid(row=0, column=0, columnspan=3, sticky=E) # This just puts it in the window, on r ow 0, col 0. If you want to learn more look up a tkinter tutorial :)
    headingL = Label(signinwindow, text='\nWelcome to the Password Management System. We need you to enter a UserName/Password which will be asked each time you want to view stored passwords.\n',justify='left',wraplength=590, font="Helvetica 14") # This just does the same as above, instead with the text new username.
    headingL.grid(row=1, column=0, columnspan=3, rowspan=3,sticky=W) # Same thing as the instruction var just on different rows. :) Tkinter is like that.
    showSignature()
#username
    userL = Label(signinwindow, text='UserName: ',font="Helvetica 13 bold") # ""
    userL.grid(row=4, column=0, sticky=W) # ""
    
    userE = Entry(signinwindow,bg="lightgray",textvariable=userE) # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    userE.grid(row=4, column=1) # ^^
#password
    pwordL = Label(signinwindow, text='Password:  ',font="Helvetica 13 bold") # ""
    pwordL.grid(row=5, column=0, sticky=W) # ""
    pwordE = Entry(signinwindow, bg="lightgray") # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    pwordE.grid(row=5, column=1) # ^^
#signin
    signupButton = Button(signinwindow, text='sign in', fg="black" ,bg="skyblue")#, command=storeGlobalPwd) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    signupButton.grid(row=6,column=3, sticky=W)
#back to register page:
    backButton = Button(signinwindow, text='back to registration', fg="black" ,bg="skyblue",command=showWindow)#, command=storeGlobalPwd) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    backButton.grid(row=7,column=3, sticky=W)
    
    signinwindow.mainloop()


global pwordE # These globals just make the variables global to the entire script, meaning any definition can use them.
global login
global roots
roots = Tk() # This creates the window, just a blank one.
roots.title('Password Management System') # This renames the title of said window to 'signup'
roots.geometry('650x400')
roots.resizable(0,0)


#this creates a menu
menubar = tk.Menu(roots)
roots.config(menu=menubar)

settingsMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Menu", menu=settingsMenu)
settingsMenu.add_command(label="About", command=about)
settingsMenu.add_separator()
settingsMenu.add_command(label="Exit", command=exitWindow)
#Instruction
instruction = Label(roots, text='Please Enter New Credentials',justify='center',  font="Helvetica 20 bold", bg="skyblue") # This puts a label, so just a piece of text saying 'please enter blah5
instruction.grid(row=0, column=0, columnspan=5, sticky=EW) # This just puts it in the window, on r ow 0, col 0. If you want to learn more look up a tkinter tutorial :)
headingL = Label(roots, text='\nWelcome to Passworx. We need you to enter a global UserName/Password which will be asked each time you want to view \nstored passwords.\n',justify='left',wraplength=590, font="Helvetica 14") # This just does the same as above, instead with the text new username.
headingL.grid(row=1, column=0, columnspan=5, rowspan=3,sticky=W) # Same thing as the instruction var just on different rows. :) Tkinter is like that.
showSignature()
#username
l1 = Label(roots, text='Name: ',font="Helvetica 13 bold") # ""
l1.grid(row=4, column=0, sticky=W) # ""
name=StringVar() 
e1 = Entry(roots,bg="lightgray",textvariable=name) # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
e1.grid(row=4, column=1,sticky="we") # ^^  
#Global UserName
l2 = Label(roots, text='Global UserName: ',font="Helvetica 13 bold") # ""
l2.grid(row=5, column=0, sticky="W") # ""
global_user_name=StringVar()
e2 = Entry(roots,bg="lightgray",textvariable=global_user_name) # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
e2.grid(row=5, column=1,sticky="we") # ^^
#Global Password:
l3 = Label(roots, text='Global Password:  ',font="Helvetica 13 bold") # ""
l3.grid(row=6, column=0, sticky=W) # ""
global_password=StringVar()   
def toggle_password():
    global e4, checkbutton
    if checkbutton.var.get():
        e3['show'] = "*" #emoji uni-code	
    else:
        e3['show'] = ""
    #checkbox for password:
checkbutton = tk.Checkbutton(roots,text="Hide password",onvalue=True,offvalue=False,command=toggle_password)                                                                                  
e3 = tk.Entry(roots,bg="lightgray",textvariable=global_password)
e3.default_show_val = e3['show']
e3['show'] = "*" #to show emoji:
checkbutton.var = tk.BooleanVar(value=True) #
checkbutton['variable'] = checkbutton.var
e3.grid(row=6,column=1,sticky="We")
e3.config(font=("Courier", 12))
checkbutton.grid(row=6,column=2)
#Email
l4 = Label(roots, text='Email: ',font="Helvetica 13 bold") # ""
l4.grid(row=7, column=0, sticky=W) # ""
email=StringVar()     
e4 = Entry(roots,bg="lightgray",textvariable=email) # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
e4.grid(row=7, column=1,sticky="we") # ^^

#signIn
signIN = Label(roots, text='Already have an account? ',font="Helvetica 13 bold") # ""
signIN.grid(row=9, column=0, sticky=W,pady="50",padx="10") # ""
signE = Button(roots,text='Sign In',fg="black",bg="skyblue", command=signin) # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
signE.grid(row=9, column=0,sticky="SEW",padx="10",pady="20") # 


#SignUp
registerButton = Button(roots, text='Register', fg="black" ,bg="skyblue",command=adder)#, command=storeGlobalPwd) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
registerButton.grid(row=9,column=1,sticky="nwe",pady="20")

roots.mainloop() # This just makes the window keep open, we will destroy it soon

    





#login  <<<<<<<<<<<<<<<<<<<< LOGIN PAGE IF ACC EXISTS >>>>>>>>>>>>>>>>>>>>>>>>>
 # This just makes the window keep open, we will destroy it soon


