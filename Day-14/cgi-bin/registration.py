#!C:/Python36/python.exe

import cgi
import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='', db='tpddl', autocommit=True)

cursor = connection.cursor()

form = cgi.FieldStorage()

username = form.getvalue('u_name')
useremail = form.getvalue('u_mail')
userpwd = form.getvalue('u_pwd')
usercity = form.getvalue('u_city')

def display(username):
    print("Content-type:text/html\r\n\r\n")
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    <h1>Registered Successfully</h1>
    <h2>Welcome {}</h2>
    </body>
    </html>
    """.format(username))

def register():
    query = 'INSERT INTO users VALUES (%s, %s, %s, %s)'
    cursor.execute(query, (username, useremail, userpwd, usercity))

    display(username)

register()