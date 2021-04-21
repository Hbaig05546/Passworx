import string
import random

def fungen():
    s1 = string.ascii_letters
    s2 = string.digits
    s3 = string.punctuation
    plen=int(input("Enter length of password\n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    random.shuffle(s)
    print("your password is\n")
    print("".join(s[0:plen]))

fungen()

