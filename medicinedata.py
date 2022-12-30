import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="root")
cr = mydb.cursor()
q = "create database medicine_shop"
cr.execute(q)
q = "use medicine_shop"
cr.execute(q)
q = '''create table medicine(
    mid integer primary key,
    mname varchar(30) not null,
    manufacturer varchar(50),
    dateofm date,
    dateofexp date not null,
    mg float,
    content varchar(100),
    price float,
    qty integer)'''
cr.execute(q)
q = '''
    create table bill(
    billid integer primary key,
    cname varchar(50),
    medicine_bought varchar(100),
    amount float,
    billdate date)'''
cr.execute(q)

mydb.commit()
print("Database Initialised")
