
# This file displays the signup screen
from tkinter import *
import tkinter as tk
from tkinter import scrolledtext as st
import f
import m

# This function is used to check if this module was imported correctly or not.
def works():
    return True


def showWindow():
    global pwordE # These globals just make the variables global to the entire script, meaning any definition can use them.
    global roots
    roots = Tk() # This creates the window, just a blank one.
    roots.title('Password Management System') # This renames the title of said window to 'signup'
    roots.geometry('500x200')
    roots.resizable(0,0)

    #this creates a menu
    menubar = tk.Menu(roots)
    roots.config(menu=menubar)

    settingsMenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Menu", menu=settingsMenu)
    settingsMenu.add_command(label="About", command=about)
    settingsMenu.add_separator()
    settingsMenu.add_command(label="Exit", command=exitWindow)

    instruction = Label(roots, text='Please Enter New Credentials',  font="Helvetica 20 bold") # This puts a label, so just a piece of text saying 'please enter blah5
    instruction.grid(row=0, column=0, columnspan=3, sticky=E) # This just puts it in the window, on r ow 0, col 0. If you want to learn more look up a tkinter tutorial :)
    headingL = Label(roots, text='\nWelcome to the Password Management System. We need you to enter a global password which will be asked each time you want to view stored passwords.\n',justify='left',wraplength=300) # This just does the same as above, instead with the text new username.
    headingL.grid(row=1, column=0, columnspan=3, rowspan=3,sticky=W) # Same thing as the instruction var just on different rows. :) Tkinter is like that.
    showSignature()

    pwordL = Label(roots, text='Global Password: ') # ""
    pwordL.grid(row=5, column=0, sticky=W) # ""
    pwordL = Label(roots, text='Global Username: ') # ""
    pwordL.grid(row=4, column=0, sticky=W) # ""
    # nameE = Entry(roots) # This now puts a text box waiting for input.
    # nameE.grid(row=1, column=1) # You know what this does now :D
    pwordE = Entry(roots, show='*') # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    pwordE.grid(row=5, column=1) # ^^
    
    pword = Entry(roots, show='*') # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    pword.grid(row=4, column=1) # ^^

    signupButton = Button(roots, text='Continue', fg="green", command=storeGlobalPwd) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    signupButton.grid(row=5,column=3, sticky=W)
    roots.mainloop() # This just makes the window keep open, we will destroy it soon

    #nameE.get()

def storeGlobalPwd():
    import ap
    import m
    ap.genSalt()
    pwd = ap.encrypt(pwordE.get()) # encrypt the given password
    ap.storeGlobal(pwd)
    f.createDataFile()
    roots.destroy() # This will destroy the signup window. :)
    m.showWindow()

# This fucntion adds our signature
def showSignature():
    text = 'Group09\n\t Guide: Prof. Abdussalam Shaikh \n\n\tMembers: \n\t Hamzah Khalid Baig   [19CO20] \n\t Uzair Shahid Kazi    [19CO22] \n\t Aaftab Harun khan    [19CO23] \n\t Mohammad Ziya-ul-Haq [19CO37]'
    return text

# This function displays the about
def about(*event):
    global aboutWindow

    aboutWindow = Tk()
    aboutWindow.title("About the developers")
    aboutWindow.geometry("600x300")
    aboutWindow.resizable(500,500)

    aboutText = showSignature()

    paper = st.ScrolledText(aboutWindow, width=350, height=200, font=("Consolas", 11))
    paper.insert("1.0", aboutText)
    paper.configure(state='normal')
    paper.pack()

    aboutWindow.mainloop()

#This function destroys the main window
def exitWindow(*event):
    roots.destroy()
