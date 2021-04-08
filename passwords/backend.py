"""
This is a backend program for the haccpsswd 
tkinter frontend.
"""
#import reqd:
import sqlite3 as sq
import datetime
import os
import sys

#making functions:

#function for connecting to the database:
def connect(person_file):
    con = sq.connect("person_account_files/%s.db"%person_file)
    cur = con.cursor() 
    cur.execute("CREATE TABLE IF NOT EXISTS Account('uniqueID' INTEGER PRIMARY KEY  ,Account_Name TEXT, UserId TEXT, 'Password' TEXT, Note TEXT ,'Date_time' TEXT)")
    con.commit() 
    con.close()
#connect() #necessary to call or the table will not be created

#function for adding:
today_date = datetime.date.today()#to convert into dd mm yyyy
new_today_date = today_date.strftime("%d/%m/%Y")       
date_data = str(new_today_date)#adding datevariable outside def indent.  

def add(person_file,Account_Name,userid,password,note,date):
    con = sq.connect("person_account_files/%s.db"%person_file)
    cur = con.cursor()
    cur.execute("INSERT INTO Account VALUES(NULL,?,?,?,?,?)",(Account_Name,userid,password,note,date))
    con.commit()
    con.close()

#function to delete:
def remove(person_file,uniqueID):
    con = sq.connect("person_account_files/%s.db"%person_file)
    cur = con.cursor()
    cur.execute("DELETE FROM Account WHERE uniqueID=?",(uniqueID,)) #dont forget the comma.:)))
    con.commit()
    con.close()

#function to search entry:
def search(person_file,account='',userid='',note=''):
    con = sq.connect("person_account_files/%s.db"%person_file)
    cur = con.cursor()
    cur.execute("SELECT * FROM Account WHERE Account_Name=? OR UserId=? OR Note=?",(account,userid,note)) 
    data = cur.fetchall()
    # con.commit()....no need to save any thing
    con.close()
    return data
    
#function to veiw_all entries:
def view(person_file):
    con = sq.connect("person_account_files/%s.db"%person_file)
    cur = con.cursor()
    cur.execute("SELECT * FROM Account ") 
    data_all = cur.fetchall()
    # con.commit()....no need to save any thing
    con.close()
    return data_all

#fuction to update entry:
def update(person_file,account,userid,password,note,date,uniqueID):
    con = sq.connect("person_account_files/%s.db"%person_file)
    cur = con.cursor()
    cur.execute("UPDATE Account SET Account_Name=?,UserId=?,'Password'=?,Note=?,'Date_time'=? WHERE uniqueID=?",(account,userid,password,note,date,uniqueID))
    con.commit()
    con.close()
    print("successfully updated account to : ?   \n",(account))

#function to clearall the database
def clear_all(person_file):
    
    con = sq.connect("person_account_files/%s.db"%person_file)
    cur = con.cursor()
    cur.execute("DELETE FROM Account") #don't forget the comma.:)))
    con.commit()
    con.close()
    print("successfully cleared all entries    \n")





#calling all function:
#add('account','name','userid','password','note',date_data)
#clear_all()
#print(view())
#print(search(name='name'))
#remove(4)
#update('qwfwfef','namwfew','useridwefewf','passwordfewfe','notewef','dateefw',12)

    
