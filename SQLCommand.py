# pip install mysql-connector-python

import mysql.connector as MyCon


def Generate_Password():
    from random import choice
    password = ""

    for _ in range(8): password = password + str(choice(choice(
        [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
        [ '@', '#', '$', '%', '&']])))

    return password


def CreateAccount(name, Dob, Phone, aadhaar, father, address, amount, password=Generate_Password()):
    sql = MyCon.connect(host='localhost', user='root', passwd='12345678', database='Accounts')
    cursor = sql.cursor()
    with open(f"PassBooks/{aadhaar}.txt",'a+') as file:
        file.write(f"Account Number:{aadhaar}\n\n")
    cursor.execute(f"Insert into accounts values('{name}', '{Dob}', {Phone}, {aadhaar}, '{father}', '{password}', \
                   '{address}', 'C:/Users/progr/Desktop/Bank/Backend/PassBooks/{aadhaar}.txt'\
                   , {amount})")
    sql.commit()
    return password


def loginAccount(userid, password):
    sql = MyCon.connect(host='localhost', user='root', passwd='12345678', database='Accounts')
    cursor = sql.cursor()
    from Transaction_Page import start_transaction as sttr
    cursor.execute(f'select PASSWORD from accounts where AADHAAR={userid}')
    if password == cursor.fetchone()[0]:
        cursor.execute(f'select Amount from accounts where AADHAAR={userid}')
        sttr(userid, int(cursor.fetchone()[0]))
        


def transaction(aadhar, amount):
    sql = MyCon.connect(host='localhost', user='root', passwd='12345678', database='Accounts')
    cursor = sql.cursor()
    cursor.execute(f"update accounts set Amount={amount} where AADHAAR={aadhar}")
    sql.commit()
    exit()
