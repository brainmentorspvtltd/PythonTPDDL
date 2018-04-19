import pymysql

connection = pymysql.connect(host='localhost', port=3306,
                             user='root', passwd='',
                             db='tpddl',
                             autocommit=True)

cursor = connection.cursor()

username = "Shyam"
usermail = "shyam@gmail.com"
userpwd = "shyam1234"
usercity = "agra"

# query = 'INSERT INTO users VALUES ("Ram","ram@gmail.com","ram1234","pune")'
query = 'INSERT INTO users VALUES (%s, %s, %s, %s)'
cursor.execute(query,(username,usermail,userpwd,usercity))