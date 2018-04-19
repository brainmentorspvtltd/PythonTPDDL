import pymysql

connection = pymysql.connect(host='localhost', port=3306,
                             user='root', passwd='',
                             db='tpddl',
                             autocommit=True)

cursor = connection.cursor()

query = 'CREATE TABLE products(p_id VARCHAR(100),p_name VARCHAR(200), p_price INT(255), p_image BLOB)'

cursor.execute(query)