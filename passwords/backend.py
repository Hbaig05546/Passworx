"""
This is a backend program for the haccpsswd 
tkinter frontend.
"""
# import reqd:
import mysql.connector as sq
import datetime
import os
import sys

# making functions:

# function for connecting to the database:

class test_db:
    def __init__(self):
        self.create_database()
        
    def create_database(self):
        self.con = sq.connect(
                                host="localhost",
                                user="root",
                                password="toor",
                                database="accpsswd"
                                )
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Person (PersonId int PRIMARY KEY AUTO_INCREMENT, Name_ VARCHAR(30) NOT NULL, Global_user_name VARCHAR(20) UNIQUE NOT NULL, Global_Password VARCHAR(50) NOT NULL,Email VARCHAR(50) UNIQUE NOT NULL,Mobile VARCHAR(13) UNIQUE NOT NULL)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS Accounts (uniqueID int PRIMARY KEY AUTO_INCREMENT ,Account_Name TEXT, UserId TEXT, Password TEXT, Note TEXT ,Date_time TEXT,Person_Id int,FOREIGN KEY (Person_Id) REFERENCES Person(PersonId))")
          
        self.con.commit()

class top_Database:
    def __init__(self):
        self.con = sq.connect(
                                host="localhost",
                                user="root",
                                password="toor",
                                database="accpsswd"
                                )
        self.cur = self.con.cursor()
        # self.cur.execute(
        #     "CREATE TABLE IF NOT EXISTS Person (PersonId int PRIMARY KEY AUTO_INCREMENT, Name_ VARCHAR(30) NOT NULL, Global_user_name VARCHAR(20) UNIQUE NOT NULL, Global_Password VARCHAR(50) NOT NULL,Email VARCHAR(50) UNIQUE NOT NULL,Mobile VARCHAR(13) UNIQUE NOT NULL)")
        # self.cur.execute("ALTER TABLE Accounts ADD IF NOT EXISTS Person_Id int")
        # self.cur.execute("ALTER TABLE Accounts IF NOT EXISTS FOREIGN KEY (Person_Id) REFERENCES Person(PersonId)")
        # self.con.commit()

    # function for adding:
    today_date = datetime.date.today()  # to convert into dd mm yyyy
    new_today_date = today_date.strftime("%d/%m/%Y")
    date_data = str(new_today_date)  # adding datevariable outside def indent.

    def add(self,name, global_user_name, Global_Password, email,mobile):
        self.cur.execute("INSERT INTO Person (Name_, Global_user_name, Global_Password, Email, Mobile) VALUES (%s,%s,%s,%s,%s)",(name, global_user_name, Global_Password, email, mobile))
        self.con.commit() 

    # function to delete:
    def remove(self, PersonId):
        # dont forget the comma.:)))
        self.cur.execute("DELETE FROM Person WHERE PersonId=%s",(PersonId,))
        self.con.commit()

    # fuction to update entry:
    def update(self, account, userid, password, note, date, uniqueID):
        self.cur.execute("UPDATE Accounts SET Account_Name=%s, UserId=%s, Password=%s, Note=%s, Date_time=%s WHERE uniqueID=%s",
                         (account, userid, password, note, date, uniqueID))
        self.con.commit()
        print("successfully updated account to : %s   \n", (account))
        
    def security_check(self,Global_user_name,Global_Password):
        self.cur.execute("SELECT * FROM Person WHERE Global_user_name=%s AND Global_Password=%s",(Global_user_name,Global_Password)) 
        data = self.cur.fetchall() #data is a list which will have length only if record is found id id an password match with database records.
        # con.commit()....no need to save any thing
        if len(data)>0:
            return True   #print(security_check("hbaig055","123"))
        else:
            return False

    def get_name_or_id(self,Global_user_name,is_name=True):
        
        self.cur.execute("SELECT PersonId,Name_ FROM Person WHERE Global_user_name=%s",(Global_user_name,))  # Don't remove the , because Since you are using mysql module, cur.execute requires a tuple as parameters
        # self.cur.execute("SELECT Name_ from Person where Global_user_name=%s",(Global_user_name))
        name = self.cur.fetchone() # fetchall() => [(1,asd)], fetchone => (1,as)
        name = list(name)
        print(name)

        if is_name:
            return name[1]
        else:
            return name[0]
        


class DataBase:
    def __init__(self):
        self.con = sq.connect(
                                host="localhost",
                                user="root",
                                password="toor",
                                database="accpsswd"
                             )
        self.cur = self.con.cursor()
        # self.cur.execute("CREATE TABLE IF NOT EXISTS Accounts (uniqueID int PRIMARY KEY AUTO_INCREMENT ,Account_Name TEXT, UserId TEXT, Password TEXT, Note TEXT ,Date_time TEXT)")
                         
        # self.con.commit()

    # function for adding:
    today_date = datetime.date.today()  # to convert into dd mm yyyy
    new_today_date = today_date.strftime("%d/%m/%Y")
    date_data = str(new_today_date)  # adding datevariable outside def indent.

    def add(self, Account_Name, userid, password, note, date,person_id):
    
        self.cur.execute("INSERT INTO Accounts (Account_Name, UserId, Password, Note, Date_time,Person_Id) VALUES (%s,%s,%s,%s,%s,%s)",
                         (Account_Name, userid, password, note, date,person_id))
        self.con.commit()

    # function to delete:
    def remove(self, uniqueID):
        # dont forget the comma.:)))
        self.cur.execute("DELETE FROM Accounts WHERE uniqueID=%s", (uniqueID,))
        self.con.commit()

    # function to search entry:
    def search(self, account='', userid='', note='', person_id=''):
        self.cur.execute(
            "SELECT * FROM Accounts WHERE Account_Name=%s OR UserId=%s OR Note=%s AND Person_Id=%s ", (account, userid, note,person_id))
        data = self.cur.fetchall()
        # con.commit()....no need to save any thing
        return data

    # function to veiw_all entries:
    def view(self,person_id):
        self.cur.execute("SELECT * FROM Accounts where Person_Id =%s ",(person_id,))
        data_all = self.cur.fetchall()
        # con.commit()....no need to save any thing
        return data_all

    # fuction to update entry:
    def update(self, account, userid, password, note, date, uniqueID):
        self.cur.execute("UPDATE Accounts SET Account_Name=%s, UserId=%s, Password=%s, Note=%s, Date_time=%s WHERE uniqueID=%s",
                         (account, userid, password, note, date, uniqueID))
        self.con.commit()
        print("successfully updated account to : %s   \n", (account))

    # function to clearall the database
    def clear_all(self,person_id):
        self.cur.execute("DELETE FROM Accounts where Person_Id=%s",(person_id,))  # don't forget the comma.:)))
        self.con.commit()
        print("successfully cleared all entries    \n")

    # calling all function:
    # add('account','name','userid','password','note',date_data)
    # clear_all()
    # print(view())
    # print(search(name='name'))
    # remove(4)
    # update('qwfwfef','namwfew','useridwefewf','passwordfewfe','notewef','dateefw',12)


# #database testing:
# mydb = sq.connect(
#   host="localhost",
#   user="root",
#   password="toor",
#   database="accpsswd"
 
# )
# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE IF NOT EXISTS Accounts (uniqueID int NOT NULL AUTO_INCREMENT ,Account_Name varchar(30), UserId varchar(30), Password varchar(30), Note varchar(255) ,Date_time varchar(10), PRIMARY KEY(uniqueID))")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)