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
# p = [85000,24000]
# p = ['Apple','Redmi']

# name == 'Apple'
# for data in products:
#     if data['name'] == 'Apple':
#         print(data)

# data = list(filter(lambda data : data['name'] == 'Apple', products))
# for d in data:
#     print(d)

# def abc(x):
#     return x['name']

data = sorted(products, key=lambda x : x['price'], reverse=True)
# print(data)
for d in data:
    print(d)
