import mysql.connector
db1 = None
def connect():
    global db1
    db1 = mysql.connector.connect(host="localhost",user="root",
    password="root",
    database = "library"
  )
  

def showMembers():
    c1 = db1.cursor()
    c1.execute("select * from member")
    res = c1.fetchall()
    print("-"*40)
    print("List of Members ")
    print("-"*40)
    for val in res:
        print(val[0] + "\t" + val[1] +"\t"+val[2]+"\t"+val[3])
    print("-"*40)

def login():
    print("-" * 40)
    print("\t Library Management System")
    print("-" * 40)
    print("\t LOGIN")
    un = input("Enter User Name : ")
    pw = input("Enter Password : ")
    q = "select * from users where username = %s and passw = %s"
    val = (un,pw)
    c2 = db1.cursor()
    c2.execute(q,val)
    res = c2.fetchall()
    print("-" * 50)
    if len(res) == 0:
        print("Invalid User Name or Password ")
        print("-" * 50)
        return False
    else:
        print("Access Granted !!!")
        print("-" * 50)
        return True

    
def delMember():
  print("-" * 40)
  print("\tDELETING A MEMBER")
  print("-" * 40)
  mid = input("Enter Member Id : ")
  cursor1 = db1.cursor()
  q = "delete from member where mid=" + mid 
  cursor1.execute(q)
  db1.commit()
  print("Member Deleted Successfully")

def addMember():
  print("-" * 50)
  print("\t ADDING A NEW MEMBER")
  print("-" * 50)
  mid = input("Enter Member Id : ")
  name = input("Enter Member Name : ")
  phone = input("Enter Phone Number : ")
  email = input("Enter Email :")
  
  cursor1 = db1.cursor()
  q = "insert into member values (%s,%s,%s,%s)"
  val = (mid,name,phone,email)
  cursor1.execute(q,val)
  db1.commit()
  print("Member Added Successfully")


def showMembers():
  cursor1 = db1.cursor()
  cursor1.execute("Select * from Member")
  res = cursor1.fetchall()
  print("-" * 50)
  print("          MEMBER DETAILS ")
  print("-" * 50)
  print("Id   Name     Email     Phone  ")
  for k in res:
    print(k[0],"  ",k[1],"  ",k[2],"  ",k[3])

def delBook():
  print("-" * 40)
  print("\tDELETING A BOOK")
  print("-" * 40)
  bid = input("Enter Book Id : ")
  cursor1 = db1.cursor()
  q = "delete from book where bookid=" + bid 
  cursor1.execute(q)
  db1.commit()
  print("Book Deleted Successfully")

def addBook():
  print("-" * 50)
  print("\t ADDING A NEW BOOK")
  print("-" * 50)
  bid = input("Enter Book Id : ")
  title = input("Enter Book Title : ")
  author = input("Enter Author name : ")
  pub = input("Enter Publisher :")
  cost = int(input("Enter Cost of the book :"))
  
  
  cursor1 = db1.cursor()
  q = "insert into book values (%s,%s,%s,%s,%s)"
  val = (bid,title,author,pub,cost)
  cursor1.execute(q,val)
  db1.commit()
  print("Book Added Successfully")


def showBooks():
  cursor1 = db1.cursor()
  cursor1.execute("Select * from Book")
  res = cursor1.fetchall()
  print("-" * 50)
  print("          BOOK DETAILS ")
  print("-" * 50)
  print("Id   Title    Author     Publisher   Cost  ")
  for k in res:
    print(k[0],"  ",k[1],"  ",k[2],"  ",k[3],"\t",k[4])



def showIssued():
    cursor1 = db1.cursor()
    cursor1.execute("Select * from issue")
    res = cursor1.fetchall()
    print("   LIST OF ISSUED BOOKS   ")
    print("-" * 40)
    print("Member   Bookid   Issue Date")
    for k in res:
        print(k[0],"\t",k[1],"\t",k[2])
    print("-" * 40)

def showReturned():
    cursor1 = db1.cursor()
    cursor1.execute("Select * from issuelog")
    res = cursor1.fetchall()
    print("   LIST OF RETURNED BOOKS   ")
    print("-" * 50)
    print("Member    Bbokid   Issue Date    Return Date")
    for k in res:
        print(k[0],"\t",k[1],"\t",k[2],"\t",k[3])
    print("-" * 50)
def issueBook():
    bid = input("Enter the book id to be issued : ")
    q ="select * from issue where bookid='" + bid +"'"
    cursor1 = db1.cursor()
    cursor1.execute(q)
    res = cursor1.fetchall()
    if len(res)== 0:
        mid = input("Enter the member id : ")
        doi = input("Enter the date of issue : ")
        q = "insert into issue (mid,bookid,dateofissue) values(%s,%s,%s)"
        data = (mid,bid,doi)
        cursor1.execute(q,data)
        db1.commit()
        print("-" * 40)
        print(" Book Issued Successfully")
        print("-" * 40)
        
        
    else:
        print("-" * 40)
        print("   Sorry ! The Book is not available")
        print("-" * 40)
        
    
def returnBook():
    bid = input("Enter the book id to be returned : ")
    mid = input("Enter the Member id : ")
    q ="select dateofissue from issue where bookid='" + bid +"' and mid='" + mid +"'"
    cursor1 = db1.cursor()
    cursor1.execute(q)
    res = cursor1.fetchall()
    if len(res)== 0:
        print("-" * 40)
        print("This Book is not Issued to This Member   ")
        print("-" * 40)
    else:
        dort = input("Enter the date of return : ")
        q = "delete from issue where bookid='" + bid + "' and mid='" + mid + "'"
        cursor1.execute(q)
        db1.commit()
        q = "insert into issuelog values(%s,%s,%s,%s)"
        data = (mid,bid,res[0][0],dort)
        cursor1.execute(q,data)
        db1.commit()
        print("Book Returned !!!")
    
connect()
print("Connected")
if login():
    while True:
        print("-" * 50)
        print("\t CHOOSE AN OPERATION ")
        print("-" * 50)
        print("Press 1 - Add a New Member")
        print("Press 2 - Delete an Existing Member")
        print("Press 3 - Show all Members")
        print("Press 4 - Add a New Book")
        print("Press 5 - Delete an Existing Book")
        print("Press 6 - Show all Books")
        print("Press 7 - Issue a Book")
        print("Press 8 - Return a Book")
        print("Press 9 - Show Issued Books")
        print("Press 10 - Show Returned Books")
        print("Press 11 - Quit")
        ch = int(input("Enter Your Choice : "))
        if ch == 1:
            addMember()
        elif ch == 2:
            delMember()
        elif ch == 3:
            showMembers()
        elif ch == 4:
            addBook()
        elif ch == 5:
            delBook()
        elif ch == 6:
            showBooks()
        elif ch == 7:
            issueBook()
        elif ch == 8:
            returnBook()
        elif ch == 9:
            showIssued()
        elif ch == 10:
            showReturned()
        elif ch == 11:
            break
