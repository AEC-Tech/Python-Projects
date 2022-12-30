# library import
import mysql.connector as sql
import time
import random as rd


def medicine():
    # function to add a medicine
    def addmedicine():
        print("\n")
        print("😇🙃" * 15)
        print("\n")
        mid = input("Enter Medicine Id : ")
        name = input("Enter Medicine Name : ")
        mf = input("Enter Name of Manufacturer : ")
        dom = input("Enter Date of Manufacture : ")
        doe = input("Enter Date of Expiry : ")
        mg = input("Enter the Weight (in mg) : ")
        content = input("Enter Content : ")
        price = input("Enter the Price : ")
        qty = input("Enter the Quantity : ")
        print("\nSTORING MEDICINE DETAILS.......")
        time.sleep(2)
        q = "insert into medicine values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        data = (mid, name, mf, dom, doe, mg, content, price, qty)
        cr = mydb.cursor()
        cr.execute(q, data)
        print("\nMedicine Inserted.......!!!!")
        print("👍😎" * 15)
        print("\n")
        mydb.commit()

    # function to show a medicine
    def showmedicine():
        print("🤩😄" * 15)
        q = "select * from medicine"
        cr = mydb.cursor()
        cr.execute(q)
        res = cr.fetchall()
        print("\n")
        print("-" * 95)
        print("Id\tName\t\tDate_of_Expiry\t\tPrice\t\tQty")
        print("-" * 95)
        for k in res:
            print(k[0], "\t", k[1], "\t\t", k[4], "\t\t", k[-2], "\t\t", k[-1])
            print("-" * 95)
        print("\n")

    # function to restock a medicine
    def restock():
        mid = input("Enter the Medicine ID : ")
        qty = input("Enter the Quantity to Add : ")
        q = "update medicine set qty = qty + %s where mid = %s"
        d = (qty, mid)
        cr = mydb.cursor()
        cr.execute(q, d)
        print("\n")
        print("😎😄" * 12)
        print("Medicine Restocked......!!")
        print("😎😄" * 12)
        print("\n")
        mydb.commit()

    # function to search a medicine
    def search():
        mid = input("Enter the Medicine ID : ")
        q = "select * from medicine where mid = " + mid
        cr = mydb.cursor()
        cr.execute(q)
        k = cr.fetchone()
        if k == None:
            print("\nNo Medicine Available With This ID\n")
            print("😣😣" * 15)
        else:
            print("\nMedicine Found......!!")
            print("😀😀" * 15)
            print("\n")
            print("-" * 95)
            print("Id\tName\t\tDate_of_Expiry\t\tPrice\t\tQty")
            print("-" * 95)
            print(k[0], "\t", k[1], "\t\t", k[4], "\t\t", k[-2], "\t\t", k[-1])
            print("-" * 95)
        print()

    # Function to delete a medicine
    def deletem():
        mid = input("Enter the Medicine ID : ")
        q = "delete from medicine where mid = " + mid
        cr = mydb.cursor()
        cr.execute(q)
        print("\nMedicine Deleted......!!\n")
        print("😒😒" * 15)
        print("\n\n")
        mydb.commit()

    # function for billing
    def billing():
        bno = input("Enter Bill No. : ")
        cname = input("Enter Customer's Name : ")
        bdate = input("Enter Bill Date (yyyy-mm-dd) : ")
        amount = 0
        medicine =""
        cr = mydb.cursor()
        while True:
            mid = input("Enter Medicine id : ")
            q = "select * from medicine where mid = " + mid
            cr.execute(q)
            res = cr.fetchone()
            if res == None:
                print("\nNo Medicine Available With This ID\n")
                print("😣😣" * 15)
            else:
                price = int(res[-2])
                medicine += res[1] + " "
                print("Price of Medicine is : ", price)
                qty = int(input("Enter the Quantity to be Purchased : "))
                bill = price * qty
                amount += bill
                print("Amount for Medicine ", amount)
                ans = input("Are There More Medicine to be Purchased : ")
                if ans.lower() == "no":
                    print("Calculating Your Bill ")
                    break
        print("Total Bill Amount is : ", amount)
        q = "insert into bill values(%s,%s,%s,%s,%s)"
        data= (bno,cname,medicine,amount,bdate)
        cr.execute(q,data)
        mydb.commit()
        print("    Bill Generated !!!    \n\n")
    def showbills():
        print("🤩😄" * 15)
        q = "select * from bill"
        cr = mydb.cursor()
        cr.execute(q)
        res = cr.fetchall()
        print("\n")
        print("-" * 95)
        print("BillNo\tName\t\tMedicine\t\t\t\tAmount\t\tDateofBill")
        print("-" * 95)
        for k in res:
            print(k[0], "\t", k[1], "\t\t", k[2], "\t\t", k[3], "\t\t", k[4])
            print("-" * 95)
        print("\n")

    while True:
        print("😇🙃" * 15)
        print("\t\t\tAL Medical Store")
        print("😇🙃" * 15)
        print("\n")
        print("Press 1 - Add New Medicine")
        print("Press 2 - Restock a Medicine")
        print("Press 3 - Show All Medicines")
        print("Press 4 - Search a Medicine")
        print("Press 5 - Delete a Medicine")
        print("Press 6 - Billing")
        print("Press 7 - Display Previous Bills")
        print("press 8 - to Exit")
        print("\n")
        opt = int(input("Enter Your Choice : "))
        if opt == 1:
            addmedicine()
        elif opt == 2:
            restock()
        elif opt == 3:
            showmedicine()
        elif opt == 4:
            search()
        elif opt == 5:
            deletem()
        elif opt == 6:
            billing()
        elif opt == 7:
            showbills()
        elif opt == 8:
            print("THANKS FOR VISITING..!!")
            print("✌😄" * 15)
            print("\t\t Have a Medicine-Free Life Ahead")
            print("*" * 95)
            break
        else:
            print("You're having only 8 options to choose -___-")
            break




# setting conection
mydb = sql.connect(host="localhost", user="root", password="root", database="medicine_shop")

# login screen
a = rd.randint(1, 9)
b = rd.randint(1, 9)
c = rd.randint(1, 9)
d = rd.randint(1, 9)
e = rd.randint(1, 9)
num = str(a) + str(b) + str(c) + str(d) + str(e)

print("\t\t", num)
n = int(input("Enter The Number Shown Above : "))
if str(n) == num:
    print("Yayyyiieee...You've Successfully Entered the Market..!!")
    if mydb.is_connected():
        print("🥳🥳🎁" * 10)
        print("\n")
        print("\t\t\tCHEMIST SHOP MANAGEMENT")
        print("\n")
        print("🥳🥳🎁" * 10)
        medicine()
        print("🙂🙃" * 15)
        print("\t\tThanks for Visiting....!!!")
        print("🙂🙃" * 15)
    else:
        print("Connection Error !!!!!")
else:
    print("Seems like it's not a human being -__-")
    print("You Can't Enter The Software. SORRY >_____<")

