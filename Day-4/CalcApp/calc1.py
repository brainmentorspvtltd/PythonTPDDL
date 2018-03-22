def add(x,y):
    result = x + y
    print("Result is",result)

def sub(x,y):
    result = x - y
    print("Result is", result)

def div(x,y):
    result = x / y
    print("Result is", result)

def mul(x,y):
    result = x * y
    print("Result is", result)

while True:
    print("""
    1. Add
    2. Sub
    3. Div
    4. Mul
    """)

    user_choice = input("Enter your choice : ")

    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))

    todo = {
        "1" : add,
        "2" : sub,
        "3" : div,
        "4" : mul
    }

    todo.get(user_choice)(num_1, num_2)

# if user_choice == "1":
#     add()
# elif user_choice == "2":
#     sub()

