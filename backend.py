"""
This is a backend program for the haccpsswd 
tkinter frontend.
"""
#import reqd:
import sqlite3 as sq
import datetime

#making functions:

#function for connecting to the database:
def connect():
    con = sq.connect("accpswd.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS exel('uniqueID' INTEGER PRIMARY KEY  ,account TEXT, name_ TEXT, userid TEXT, 'password' TEXT, note TEXT ,'date' TEXT)")
    con.commit()
    con.close()
connect()  #necessary to call or the table will not be created

#function for adding:
today_date = datetime.date.today()#to convert into dd mm yyyy
new_today_date = today_date.strftime("%d/%m/%Y")       
date_data = str(new_today_date)#adding datevariable outside def indent.  
def add(account,name,userid,password,note,date):
    con = sq.connect("accpswd.db")
    cur = con.cursor()
    cur.execute("INSERT INTO exel VALUES(NULL,?,?,?,?,?,?)",(account,name,userid,password,note,date))
    con.commit()
    con.close()

#function to delete:
def remove(uniqueID):
    con = sq.connect("accpswd.db")
    cur = con.cursor()
    cur.execute("DELETE FROM exel WHERE uniqueID=?",(uniqueID,)) #dont forget the comma.:)))
    con.commit()
    con.close()

#function to search entry:
def search(account='',name='',userid='',note=''):
    con = sq.connect("accpswd.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM exel WHERE account=? OR name_=? OR userid=? OR note=?",(account,name,userid,note)) 
    data = cur.fetchall()
    # con.commit()....no need to save any thing
    con.close()
    return data
    
#function to veiw_all entries:
def view():
    con = sq.connect("accpswd.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM exel ") 
    data_all = cur.fetchall()
    # con.commit()....no need to save any thing
    con.close()
    return data_all

#fuction to update entry:
def update(account,name,userid,password,note,date,uniqueID):
    con = sq.connect("accpswd.db")
    cur = con.cursor()
    cur.execute("UPDATE exel SET account=?,name_=?,userid=?,'password'=?,note=?,'date'=? WHERE uniqueID=?",(account,name,userid,password,note,date,uniqueID))
    con.commit()
    con.close()
    print("successfully updated account to : ?   \n",(account))

#function to clearall the database
def clear_all():
    
    con = sq.connect("accpswd.db")
    cur = con.cursor()
    cur.execute("DELETE FROM exel") #don't forget the comma.:)))
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

    
