# Built in Exceptions - ZeroDivisionError/BaseException
# User Defined - raise and assert

def home():
    print("Welcome to ICICI")
    atm()

def atm():
    userpin = input("Enter your PIN : ")
    total_bal = 10000
    try:
        if userpin == "1234":
            print("Welcome User")
        else:
            # print("Wrong PIN")
            raise ValueError("Wrong PIN")
    except ValueError as err:
        print(err)
        home()

    else:
        amount = int(input("Enter the amount you want to withdraw : "))
        total_bal = total_bal - amount
        print("Remaining Balance is",total_bal)

# atm()
home()

# def home(x):
#     print("This is home function")

# home()