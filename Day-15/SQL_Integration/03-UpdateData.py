import pymysql

connection = pymysql.connect(host='localhost', port=3306,
                             user='root', passwd='',
                             db='tpddl',
                             autocommit=True)

cursor = connection.cursor()

useremail = 'ram@gmail.com'
userpwd = 'ram1234'
updatedPwd = '1234ram'

query = "UPDATE users SET userPwd = %s WHERE userEmail = %s AND userPwd = %s"

cursor.execute(query, (updatedPwd, useremail, userpwd))