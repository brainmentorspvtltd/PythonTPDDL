import cgi
import json

form = cgi.FieldStorage()

searchVal = form.getvalue('search')
# print("You searched for",searchVal)

with open('data.json') as data_file:
    products = json.load(data_file)

searchData = list(filter(lambda d : d['name'] == searchVal, products))

print("Content-type:text/html\r\n\r\n")
print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    <h1>Search Result</h1>
    <table border=2 width=100% cellpadding=10 cellspacing=10>
        <tr>
            <th>Product Name</th>
            <th>Product Price</th>
            <th>Product Image</th>
        </tr>
""")

for data in searchData:
    print("""
            <tr class='product'>
                <td><h3>Name : {}</h3></td>
                <td><p>Price : {}</p></td>
                <td><img src={} alt="image" width=200 height=250/></td>
            </tr>                
            """.format(data['name'], data['price'], data['img']))

print("""
</body>
</html>
""")