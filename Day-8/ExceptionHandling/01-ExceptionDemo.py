def main():
    try:
        a = int(input("Enter first num : "))
        b = int(input("Enter second num : "))
        c = a + b
        d = a - b
        e = a / b
        f = a * b
        print("Result is",c)

    # except BaseException as err:
    #     print("Some error",err)

    except ValueError as err:
        print("You have typed something wrong")
        main()

    except ZeroDivisionError as err:
        print("Cannot divide by zero")
        main()

main()