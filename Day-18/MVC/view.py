from controller import *

def userdetails():
    userid = int(input("Enter your id : "))
    username = input("Enter your name : ")
    usercompany = input("Enter your company : ")
    usersal = int(input("Enter your salary  :"))

    data = controller(userid, username, usercompany, usersal)

    print("Registered Successfully")
    for d in data:
        print(d)

while True:
    userdetails()