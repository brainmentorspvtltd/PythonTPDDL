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
        <h1>{}</h1>
        """.format(data))
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