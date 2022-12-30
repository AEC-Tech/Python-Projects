import mysql.connector as mycon
con = mycon.connect(host="localhost",user="root",password="root",database="hotel")

def showmenu():
    while True:
        print("@" * 30)
        print("----    HOTEL AWANA    ----")
        print("@" * 30)
        print("Press 1 - Create a New Room")
        print("Press 2 - Show All Rooms")
        print("Press 3 - Show All Vacant Rooms")
        print("Press 4 - Show All Occupied Rooms")
        print("Press 5 - Book a Room")
        print("Press 6 - Check Out")
        print("Press 7 - Exit")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            createRoom()
        elif choice == 2:
            showRooms()
        elif choice == 3:
            showVacantRooms()
        elif choice == 4:
            showOccupiedRooms()
        elif choice == 5:
            bookRoom()
        elif choice == 6:
            checkout()
        elif choice == 7:
            break
def createRoom():
    print(" --- ENTER ROOM DETAILS  --- ")
    rno = int(input("Enter Room No. : "))
    type = input("Enter Room Type(Simple/Delux/Super Delux):")
    guest = int(input("Enter maximum number of guests : "))
    loc = input("Enter Location details : ")
    rent = int(input("Enter Per Day Charges : "))
    status = "Vacant"
    q = "insert into rooms values(%s,%s,%s,%s,%s,%s)"
    data = (rno,type,loc,guest,rent,status)
    cr1 = con.cursor()
    cr1.execute(q,data)
    con.commit()
    print("---  Room Created Successfully  ---")

def showRooms():
    q = "select * from rooms"
    cr1 = con.cursor()
    cr1.execute(q)
    res = cr1.fetchall()
    for row in res:
        print(row)

def showVacantRooms():
    q = "select * from rooms where status='Vacant'"
    cr1 = con.cursor()
    cr1.execute(q)
    res = cr1.fetchall()
    for row in res:
        print(row)

def showOccupiedRooms():
    q = "select room_no, cname, phone from rooms,booking where status='Occupied' and romm_no = room_no"
    cr1 = con.cursor()
    cr1.execute(q)
    res = cr1.fetchall()
    for row in res:
        print(row)

def bookRoom():
    print("-" * 40)
    print("       BOOKING A ROOM ")
    print("-" * 40)
    cname = input("Enter the Customer Name : ")
    idtype = input("Enter the ID submitted(PAN Card/License/Aadhar Card/Passport) : ")
    idno = input("Enter the ID number : ")
    address = input("Enter Address : ")
    phone = input("Enter Phone number : ")
    gender = input("Enter Gender : ")
    dcheckin = input("Enter Date of Check in (yyyy-mm-dd) : ")
    room_no = int(input("Enter Room number : "))
    q = "insert into booking(cname,idno,idtype,address,phone,gender,dateofcheckin,room_no) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    data = (cname,idno,idtype,address,phone,gender,dcheckin,room_no)
    cr = con.cursor()
    cr.execute(q,data)
    con.commit()
    q = "update rooms set status='Occupied' where romm_no ="+ str(room_no)
    cr.execute(q)
    con.commit()
    print("-" * 50)
    print("      ROOM BOOKED")
    print("-" * 50)

#Function to checkout a guest
def checkout():
     room_no = input("Enter the Room Number : ")
     q = "select room_no, cname, phone from rooms,booking where status='Occupied' and romm_no ="+ room_no
     cr1 = con.cursor()
     cr1.execute(q)
     res = cr1.fetchall()
     for row in res:
         print(row)
     chkoutdate = input("Enter the date of Checkout : ")
     q = "update rooms set status='Vacant' where romm_no =" + str(room_no)
     cr1.execute(q)
     con.commit()
if con.is_connected():
    showmenu()