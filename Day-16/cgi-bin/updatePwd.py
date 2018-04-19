#!C:/Python36/python.exe

import cgi
import pymysql

connection = pymysql.connect(host='localhost', port=3306,
                             user='root', passwd='',
                             db='tpddl',
                             autocommit=True)
cursor = connection.cursor()
form = cgi.FieldStorage()
useremail = form.getvalue('up_email')
updatedpwd = form.getvalue('up_pwd')

def show():
    print("Content-type:text/html\r\n\r\n")
    print("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
        <h1>Password Updated Successfully</h1>
        </body>
        </html>
        """)

def updatePassword():
    query = "UPDATE users SET userPwd = %s WHERE userEmail = %s"
    cursor.execute(query, (updatedpwd, useremail))
    # cursor.rowcount

    show()

updatePassword()