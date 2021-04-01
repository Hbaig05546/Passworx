#import reqd:
import mysql as sq
import datetime

 
def connect():
    con = sq.connect("accpswd.db")
    cur = con.cursor() 
    cur.execute("CREATE TABLE IF NOT EXISTS Person('uniqueID' INT PRIMARY KEY ,Name_ VARCHAR(30) NOT NULL , Global_user_name VARCHAR(20) UNIQUE NOT NULL, 'Global_Password' VARCHAR(50) NOT NULL,'Email' VARCHAR(50) UNIQUE NOT NULL)")
    con.commit() 
    con.close()
connect()

#function for adding:
today_date = datetime.date.today()#to convert into dd mm yyyy
new_today_date = today_date.strftime("%d/%m/%Y")       
date_data = str(new_today_date)#adding datevariable outside def indent.  

def add(name, global_user_name, Global_Password, email):
    con = sq.connect("accpswd.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Person VALUES(NULL,?,?,?,?)",(name, global_user_name, Global_Password, email))
    con.commit()
    con.close()
    print("row added: %s, %s, %s, %s"%(name,global_user_name, Global_Password, email))

def remove(uniqueID):
    con = sq.connect("accpswd.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Person WHERE uniqueID=?",(uniqueID,)) #dont forget the comma.:)))
    con.commit()
    con.close()

def view():
    con = sq.connect("accpswd.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Person ") 
    data_all = cur.fetchall()
    # con.commit()....no need to save any thing
    con.close()
    return data_all

def update(account,name,userid,password,note,date,uniqueID):
    con = sq.connect("accpswd.db")
    cur = con.cursor()
    cur.execute("UPDATE exel SET account=?,name_=?,userid=?,'password'=?,note=?,'date'=? WHERE uniqueID=?",(account,name,userid,password,note,date,uniqueID))
    con.commit()
    con.close()
    print("successfully updated account to : ?   \n",(account))



def security_check(Login_Id,Global_Password):
        con = sq.connect("accpswd.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM Person WHERE Login_Id=? AND Global_Password=?",(Login_Id,Global_Password)) 
        data = cur.fetchall() #data is a list which will have length only if record is found id id an password match with database records.
        # con.commit()....no need to save any thing
        con.close()
        if len(data)>0:
            return True   #print(security_check("hbaig055","123"))
        else:
            return False

def format():
    con = sq.connect("accpswd.db")
    cur = con.cursor()
    cur.execute("DROP TABLE Person")
    con.commit()
    con.close()



con = sq.connect("accpswd.db")
cur = con.cursor()
cur.execute("SELECT * FROM Person")
data = cur.fetchall()
for i in data:
    print(i)
con.commit()
con.close()



