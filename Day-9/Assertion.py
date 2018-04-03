def atm():
    total_bal = 10000
    amount = int(input("Enter the amount you want to withdraw : "))

    try:
        assert (total_bal > amount), "You donot have sufficient balance"
    except AssertionError as err:
        print(err)
    else:
        total_bal = total_bal - amount
        print("Total Balance is", total_bal)

atm()