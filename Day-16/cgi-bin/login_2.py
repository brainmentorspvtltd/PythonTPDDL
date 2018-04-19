#!C:/Python36/python.exe

import cgi
import pymysql
import json

connection = pymysql.connect(host='localhost', port=3306,
                             user='root', passwd='',
                             db='tpddl',
                             autocommit=True)

cursor = connection.cursor()

form = cgi.FieldStorage()

useremail = form.getvalue('login_id')
userpwd = form.getvalue('login_pwd')

with open('data.json') as data_file:
    products = json.load(data_file)

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
    <form action='searchData.py' method='post'>
        <input type='text' placeholder='Search Product' name='search'>
        <input type='submit' value='Search'>
    </form>
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