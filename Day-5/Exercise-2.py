products = [
    {'id': 101,'name':'Apple','price':85000,'color':'white'},
    {'id': 102,'name':'Samsung','price':55000,'color':'silver'},
    {'id': 103,'name':'Vivo','price':22000,'color':'silver'},
    {'id': 104,'name':'Redmi','price':12000,'color':'black'},
    {'id': 105,'name':'Apple','price':65000,'color':'black'},
    {'id': 106,'name':'Vivo','price':20000,'color':'white'},
    {'id': 107,'name':'Samsung','price':35000,'color':'white'},
    {'id': 108,'name':'Samsung','price':38000,'color':'silver'},
    {'id': 109,'name':'Vivo','price':27000,'color':'Black'},
    {'id': 110,'name':'Redmi','price':13000,'color':'White'},
]

def search():
    searchVal = input("Enter your search : ")

    data = list(filter(lambda x : x['name'] == searchVal, products))
    for d in data:
        print(d)

def sort():
    print("""
    1. High to low
    2. Low to High
    """)
    user_ch = input("Enter your choice : ")
    sort_by = input("Sort By name or price : ")
    if user_ch == "1":
        data = sorted(products, key=lambda x: x[sort_by],reverse=True)
        for d in data:
            print(d)
    else:
        data = sorted(products, key=lambda x: x[sort_by])
        for d in data:
            print(d)

def errHandler():
    print("Wrong Choice...")

while True:
    print("""
    1. Search
    2. Sort
    """)

    user_choice = input("Enter your choice : ")

    todo = {
        "1" : search,
        "2" : sort
    }
    # get(success,failure)
    todo.get(user_choice,errHandler)()
