import mysql.connector
db1 = None
def connect():
    global db1
    db1 = mysql.connector.connect(host="localhost",user="root",
    password="root"
  )

connect()
c1 = db1.cursor()
c1.execute("drop database library")
c1.execute("create database library")
c1.execute("use library")
c1.execute("create table users (username varchar(30), passw varchar(30))")
c1.execute("insert into users values('Anjali','abc123')")
c1.execute("insert into users values('Rahul','xyz123')")
c1.execute("insert into users values('Aarav','pqr123')")
db1.commit()
c1.execute("create table member(mid varchar(20) primary key,name varchar(50),email varchar(50), phone varchar(20))")
c1.execute("create table book(bookid varchar(20) primary key,title varchar(50), author varchar(50), publisher varchar(50), cost integer)")
c1.execute("create table issue(mid varchar(20), bookid varchar(20), dateofissue date)")
c1.execute("create table issuelog(mid varchar(20), bookid varchar(20), dateofissue date, dateofreturn date)")

db1.commit()
