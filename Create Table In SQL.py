import mysql.connector as MyCon
sql = MyCon.connect(host='localhost', user='root', passwd='password', database='Accounts')

cursor = sql.cursor()

cursor.execute("create database accounts")
sql.commit()

cursor.execute('use accounts')
sql.commit()

cursor.execute("create table accounts(name char(50), dob char(10), Phone bigint, aadhaar bigint primary key, father char(50), password char(8), address char(200), file char(100), Amount int")
sql.commit()

sql.close()
