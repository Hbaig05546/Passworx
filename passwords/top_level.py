
# This file displays the signup screen
from tkinter import *
import tkinter as tk
from tkinter import scrolledtext as st
import threading
from backend import *
import mysql.connector as sq
import accpsswd
import re #for psswd check
import pygubu
testdb = test_db()
tlb = top_Database()
#global variables:
global checkbutton,e3,e2
global roots

def showSignature():
    text = 'Group09\n\t  \n\n\tMembers: \n\t Hamzah Khalid Baig   [19CO20] \n\t Uzair Shahid Kazi    [19CO22] \n\t Aaftab Harun khan    [19CO23] \n\t Mohammad Ziya-ul-Haq [19CO37]'
    return text

def about(*event):
    global aboutWindow
    aboutWindow = Tk()
    aboutWindow.geometry("400x200")
    aboutWindow.resizable(0,0)

    aboutText = showSignature()

    paper = st.ScrolledText(aboutWindow, width=350, height=200, font=("Consolas", 11))
    paper.insert("1.0", aboutText)
    paper.pack()
    paper.configure(state='disabled')
    

    aboutWindow.mainloop()



#<<<<<<<<<<<<<<<<<<<<<<<<<<<<!!!! SIGN-IN WINDOW FUNCTION !!!!!!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def signin(*event):
    roots.destroy()
    def exit_signin_Window(*event):
        signinwindow.destroy()
    global signinwindow # These globals just make the variables global to the entire script, meaning any definition can use them.
    signinwindow = Tk() # This creates the window, just a blank one.
    signinwindow.title('Password Management System') # This renames the title of said window to 'signup'
    signinwindow.geometry('700x300')
    signinwindow.resizable(0,0)

    def Allow_access():
        gun=global_user_name.get()  #here gun will be the name of the database file
        gp=global_password.get()
        if tlb.security_check(gun,gp):
            print("access granted")
            signinwindow.destroy()
            # accpsswd.name_holder(global_user_name.get())
            accpsswd.accpsswd(global_user_name.get())
            

        else:
            print("Wrong username or password")
            l3["text"]="!!! Incorrect Username or password :( !!!"




    #stringvars:
    global_user_name=StringVar()
    global_password=StringVar()
    #instructions
    instruction = Label(signinwindow, text='Please Enter Credentials to login',justify='center',  font="Helvetica 20 bold", bg="skyblue") # This puts a label, so just a piece of text saying 'please enter blah5
    instruction.grid(row=0, column=0, columnspan=4, sticky=E) # This just puts it in the window, on r ow 0, col 0. If you want to learn more look up a tkinter tutorial :)
    headingL = Label(signinwindow, text='\nWelcome to the Password Management System. Please Login with your Global Username and Password.\n',justify='left',wraplength=590, font="Helvetica 14") # This just does the same as above, instead with the text new username.
    headingL.grid(row=1, column=0, columnspan=3, rowspan=3,sticky=W) # Same thing as the instruction var just on different rows. :) Tkinter is like that.
    showSignature()
    
    #output label:
    l3 = Label(signinwindow, text='',font="Helvetica 13 ",fg="red") # ""
    l3.grid(row=6, column=0,columnspan=2, sticky="WENS",pady=(10,0))
    #username
    l1 = Label(signinwindow, text='UserName: ',font="Helvetica 13 bold") # ""
    l1.grid(row=4, column=0, sticky="WE") # ""
    e1 = Entry(signinwindow,bg="lightgray",textvariable=global_user_name) # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    e1.grid(row=4, column=1) # ^^
    #password
    l2 = Label(signinwindow, text='Password:  ',font="Helvetica 13 bold") # ""
    l2.grid(row=5, column=0, sticky="WE") # ""
     # ^^
    
    def toggle_password():
        
        if checkbutton.var.get():
            e2['show'] = "*" #emoji uni-code	
        else:
            e2['show'] = ""
        #checkbox for password:
    checkbutton = tk.Checkbutton(signinwindow,text="Hide password",onvalue=True,offvalue=False,command=toggle_password)                                                                                  
    e2 = Entry(signinwindow, bg="lightgray",textvariable=global_password) # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    e2.grid(row=5, column=1,sticky="WE")
    e2.default_show_val = e2['show']
    e2['show'] = "*" #to show emoji:
    checkbutton.var = tk.BooleanVar(value=True) #
    checkbutton['variable'] = checkbutton.var
    checkbutton.grid(row=6,column=1)
    #signin
    signupButton = Button(signinwindow, text='Sign In', fg="black" ,bg="skyblue",command=Allow_access)#, command=storeGlobalPwd) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    signupButton.grid(row=6,column=3, sticky=W)
    #back to register page:
    backButton = Button(signinwindow, text='back to registration', fg="black" ,bg="skyblue",command=Register_window())#, command=storeGlobalPwd) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    backButton.grid(row=7,column=3, sticky=W)
    
    signinwindow.mainloop()

#<<<<<<<<<<<<<<<<<<<<<<!!!!! REGISTER WINDOW FUNCTION !!!!!!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def Register_window(*event):
    
    #nested functions for keeping variables defined :)

    #function to test password stregth:
    
# Python program to check validation of password
# Module of regular expression is used with search()
    def entry_check(username,passwd,email,mobile):
        def userN_valid(username):
            if len(username)>=8:
                return True
        def psswd_valid(passwd):
            SpecialSym =['$', '@', '#', '%','!','^','&','*','(',')','+','-','=']
            val = True
            if len(passwd) < 8:
                l6["text"]="Password must have atleast 8 characters"
                val = False   
            if len(passwd) > 20:
                print('length should be not be greater than 20')
                
                val = False    
            if not any(char.isdigit() for char in passwd):
                l6["text"]="Password must contain \nat least one numeral [1-9]"
                val = False   
            if not any(char.isupper() for char in passwd):
                l6["text"]="Password must contain \nat least one uppercase letter [A-Z]"
                val = False  
            if not any(char.islower() for char in passwd):
                l6["text"]="Password must contain \nat least one lowercase letter [a-z]"
                val = False   
            if not any(char in SpecialSym for char in passwd):
                l6["text"]="Password must contain\nat least one special character [!@#$%^&*()+-=]"
                val = False
            if val:
                return val
                
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        def email_valid(email):
            if(re.search(regex, email)):
                return True
            else:
                return False
        def mobile_valid(mobile):
            # 1) Begins with 0 or 91
            # 2) Then contains 7 or 8 or 9.
            # 3) Then contains 9 digits
            Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
            return Pattern.match(mobile)
        if userN_valid(username) and psswd_valid(passwd) and email_valid(email) and mobile_valid(mobile):
            return True
        elif not userN_valid(username):
            l6["text"]="Invalid username. Username should contain\n atleast 8 characters"
            return False
        elif not psswd_valid(passwd):
            psswd_valid(passwd)
            return False
        elif not email_valid(email):
            l6["text"]="Invalid email. Email_id must\n be in proper format"
            return False
        elif not mobile_valid(mobile):
            l6["text"]="Invalid Mobile number.\n Mobile number should start with 91"
            return False
        else:
            print("error")



    #function to destroy window:
    def exit_register_Window(*event):
        roots.destroy()
    #database nested function and functions to get the strvars:
    def adder():
        # if entry_check(global_user_name.get(),global_password.get(),email.get(),mobile.get()):
        if True:
            try:
                tlb.add(name.get(),global_user_name.get(),global_password.get(),email.get(),mobile.get())
                signin()
            except sq.IntegrityError:
                l6["text"]="Given UserId or Email already exists"
            
        else:
            entry_check(global_user_name.get(),global_password.get(),email.get(),mobile.get())
   
    #<<<<<<<<!!!!!!!!!! REGISTER WINDOW CODE !!!!!!!!!!!>>>>>>>>>>>>
    # These globals just make the variables global to the entire script, meaning any definition can use them.
    global roots
    roots = Tk() # This creates the window, just a blank one.
    roots.title('Password Management System') # This renames the title of said window to 'signup'
    roots.geometry('700x400')
    roots.resizable(0,0)
    
    #stringvars():
    name=StringVar() 
    global_user_name=StringVar()
    global_password=StringVar() 
    email=StringVar() 
    mobile=StringVar()

    #this creates a menu
    menubar = tk.Menu(roots)
    roots.config(menu=menubar)

    settingsMenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Menu", menu=settingsMenu)
    settingsMenu.add_command(label="About", command=about)
    settingsMenu.add_separator()
    settingsMenu.add_command(label="Exit", command=exit_register_Window)
    #Instruction
    instruction = Label(roots, text='Please Enter New Credentials',justify='center',  font="Helvetica 20 bold", bg="skyblue") # This puts a label, so just a piece of text saying 'please enter blah5
    instruction.grid(row=0, column=0, columnspan=5, sticky=EW) # This just puts it in the window, on r ow 0, col 0. If you want to learn more look up a tkinter tutorial :)
    headingL = Label(roots, text='\nWelcome to Passworx. We need you to enter a global UserName/Password which will be asked each time you want to view \nstored passwords.\n',justify='left',wraplength=590, font="Helvetica 14") # This just does the same as above, instead with the text new username.
    headingL.grid(row=1, column=0, columnspan=5, rowspan=3,sticky=W) # Same thing as the instruction var just on different rows. :) Tkinter is like that.
    showSignature()
    #username
    l1 = Label(roots, text='Name: ',font="Helvetica 13 bold") # ""
    l1.grid(row=4, column=0, sticky=W) # ""
    
    e1 = Entry(roots,bg="lightgray",textvariable=name) # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    e1.grid(row=4, column=1,sticky="we") # ^^ 
    e1.config(font="helvatica 13") 
    #Global UserName
    l2 = Label(roots, text='Global UserName: ',font="Helvetica 13 bold") # ""
    l2.grid(row=5, column=0, sticky="W") # ""
    
    e2 = Entry(roots,bg="lightgray",textvariable=global_user_name) # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    e2.grid(row=5, column=1,sticky="we") # ^^
    e2.config(font="helvatica 13")
    #Global Password:
    l3 = Label(roots, text='Global Password:  ',font="Helvetica 13 bold") # ""
    l3.grid(row=6, column=0, sticky=W) # ""
      
    def toggle_password():
        if checkbutton.var.get():
            e3['show'] = "*" #emoji uni-code	
        else:
            e3['show'] = ""
        #checkbox for password:
    
    checkbutton = tk.Checkbutton(roots,text="Hide password",onvalue=True,offvalue=False,command=toggle_password)                                                                                  
    checkbutton.var = tk.BooleanVar(value=True) #
    checkbutton['variable'] = checkbutton.var
    e3 = tk.Entry(roots,bg="lightgray",textvariable=global_password)
    e3.default_show_val = e3['show']
    e3['show'] = "*" #to show emoji:
    
    e3.grid(row=6,column=1,sticky="We")
    e3.config(font="helvatica 13")
    checkbutton.grid(row=6,column=2)
    #Email
    l4 = Label(roots, text='Email: ',font="Helvetica 13 bold") # ""
    l4.grid(row=7, column=0, sticky=W) # ""
    e4 = Entry(roots,bg="lightgray",textvariable=email) # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    e4.grid(row=7, column=1,sticky="we") # ^^
    e4.config(font="helvatica 13")
    #mobile:
    l5 = Label(roots, text='Mobile: ',font="Helvetica 13 bold") # ""
    l5.grid(row=8, column=0, sticky=W) # ""
    e5 = Entry(roots,bg="lightgray",textvariable=mobile) # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    e5.grid(row=8, column=1,sticky="we")
    e5.config(font="helvatica 13")
    #output label:
    l6 = Label(roots, text='',font="Helvetica 13 ",fg="red") # ""
    l6.grid(row=9, column=1,columnspan="3", sticky="S",pady=(10,0),padx=(10,0))

    #signIn
    signIN = Label(roots, text='Already have an account? ',font="Helvetica 13 bold") # ""
    signIN.grid(row=9, column=0, sticky=W,pady=(70,0),padx=(0,20)) # ""
    signE = Button(roots,text='Sign In',fg="black",bg="skyblue", command=signin) # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    signE.grid(row=10, column=0,sticky="SEW",padx=(0,20),pady=(0,0)) # 


    #SignUp
    registerButton = Button(roots, text='Register', fg="black" ,bg="skyblue",command=adder)#, command=storeGlobalPwd) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    registerButton.grid(row=9,column=1,sticky="nwe",pady="20")

    roots.mainloop() # This just makes the window keep open, we will destroy it soon



Register_window() #STARTING REGISTER WINDOW..

# if __name__ == '__main__':
#     app = loadScreen()
#     app.run()

#login  <<<<<<<<<<<<<<<<<<<< LOGIN PAGE IF ACC EXISTS >>>>>>>>>>>>>>>>>>>>>>>>>
 # This just makes the window keep open, we will destroy it soon


