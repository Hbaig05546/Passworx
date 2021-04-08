import re
def psswd_valid(psswd):
    password = str(psswd)
    flag = True
    while True:  
        if (len(password)<8):
            flag = False 
            break
        elif not re.search("[a-z]", password):
            flag = False
            break
        elif not re.search("[A-Z]", password):
            flag = False
            break
        elif not re.search("[0-9]", password):
            flag = False
            break
        elif not re.search("[_@$]", password):
            flag = False
            break
        elif re.search("\s", password):
            flag = False
            break
        else:
            flag = True
            print("Valid Password")
            break
    if flag == False:
        print("Not a Valid Password")
        return flag


