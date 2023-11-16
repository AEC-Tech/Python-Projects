import mysql.connector
db1 = None
def connect():
    global db1
    db1 = mysql.connector.connect(host="localhost",user="root",
    password="root"
  )

connect()
c1 = db1.cursor()
#c1.execute("drop database hotel")
c1.execute("create database hotel")
c1.execute("use hotel")
c1.execute("create table rooms(romm_no integer,type varchar(50),location varchar(30),no_of_guest integer,rent integer, status varchar(20))")
c1.execute("create table billing(cname varchar(20),idtype varchar(40),idno varchar(40), address varchar(50), phone varchar(10),gender varchar(20), dcheckin date,room_no integer)")


db1.commit()
