#!C:/Python36/python.exe

import cgi

form = cgi.FieldStorage()

username = form.getvalue('u_name')
userpwd = form.getvalue('u_pwd')

def checkLogin():
    if username == userpwd:
        return "Hello "+username
    else:
        return "Login Failed"


print("Content-type:text/html\r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>{}</h1>
</body>
</html>
""".format(checkLogin()))