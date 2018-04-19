#!C:/Python36/python.exe

import cgi
import pymysql

connection = pymysql.connect(host='localhost', port=3306,
                             user='root', passwd='',
                             db='tpddl',
                             autocommit=True)

cursor = connection.cursor()

form = cgi.FieldStorage()

useremail = form.getvalue('login_id')
userpwd = form.getvalue('login_pwd')

# useremail = 'ram@gmail.com'
# userpwd = 'ram1234'

products = [
    {'id': 101,'name':'Apple','price':85000,'img':'https://cdn.homeshopping.pk/product_images/y/371/apple-iphone-7-32gb-black-XS-1__04382_zoom.jpg'},
    {'id': 102,'name':'Samsung','price':55000,'img':'https://www.jasminmobile.com/wp-content/uploads/2017/12/Note8-Front-S-Pen-Midnight-Black.jpeg'},
    {'id': 103,'name':'Vivo','price':22000,'img':'https://www.whatmobile.com.pk/admin/images/Vivo/VivoV9-b.gif'},
    {'id': 104,'name':'Redmi','price':12000,'img':'https://d2giyh01gjb6fi.cloudfront.net/default/0002/27/thumb_126161_default_big.png'},
    {'id': 105,'name':'Apple','price':65000,'img':'https://cdn.homeshopping.pk/product_images/y/371/apple-iphone-7-32gb-black-XS-1__04382_zoom.jpg'},
    {'id': 106,'name':'Vivo','price':20000,'img':'https://www.whatmobile.com.pk/admin/images/Vivo/VivoV9-b.gif'},
    {'id': 107,'name':'Samsung','price':35000,'img':'https://www.jasminmobile.com/wp-content/uploads/2017/12/Note8-Front-S-Pen-Midnight-Black.jpeg'},
    {'id': 108,'name':'Samsung','price':38000,'img':'https://www.jasminmobile.com/wp-content/uploads/2017/12/Note8-Front-S-Pen-Midnight-Black.jpeg'},
    {'id': 109,'name':'Vivo','price':27000,'img':'https://www.whatmobile.com.pk/admin/images/Vivo/VivoV9-b.gif'},
    {'id': 110,'name':'Redmi','price':13000,'img':'https://d2giyh01gjb6fi.cloudfront.net/default/0002/27/thumb_126161_default_big.png'},
]





def login(data):
    print("Content-type:text/html\r\n\r\n")
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    """)
    if useremail and userpwd in data:
        print("""
        <a href="../html/updatePwd.html">Update Password</a>
        <h1>{}</h1>
        <table border=2 width=100% cellpadding=10 cellspacing=10>
        <tr>
            <th>Product Name</th>
            <th>Product Price</th>
            <th>Product Image</th>
        </tr>
        """.format(data))

        for data in products:
            print("""
            <tr class='product'>
                <td><h3>Name : {}</h3></td>
                <td><p>Price : {}</p></td>
                <td><img src={} alt="image" width=200 height=250/></td>
            </tr>                
            """.format(data['name'], data['price'], data['img']))

        print("""
            </table>
            """)

    else:
        print("""
        <h2>Login Failed</h2>
        """)

    print("""
    </body>
    </html>
    """)

def checkLogin():
    data = list()
    query = "SELECT * FROM users WHERE userEmail = %s AND userPwd = %s"
    cursor.execute(query, (useremail,userpwd))
    for data in cursor:
        pass
    login(data)

checkLogin()