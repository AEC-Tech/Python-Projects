import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

print("---------------------------WELCOME TO LUXURY CAR RENTALS---------------------------")


def addUser():
    uid = input("Enter User ID:")
    uname = input("Enter User Name:")
    pwd = input("Enter Password:")
    udf = pd.read_csv("Users.csv")
    n = udf["User ID"].count()
    udf.at[n] = [uid, uname, pwd]
    udf.to_csv("Users.csv", index=False)
    print("User added successfully")
    print(udf)


def deleteUser():
    uid = input("Enter a User ID:")
    udf = pd.read_csv("Users.csv")
    udf = udf.drop(udf[udf["User ID"] == uid].index)
    udf.to_csv("Users.csv", index=False)
    print("User deleted successfully")
    print(udf)


def addNewCar():
    carno = int(input("Enter a Car Number:"))
    carname = input("Enter Name of the Car:")
    brand = input("Enter brand of the Car:")
    branch = input("Enter branch:")
    fueltype = input("Enter fuel type of the car:")
    cost = int(input("Enter cost of rent per day:"))
    category = input("Enter category of the car:")
    cdf = pd.read_csv("Cars.csv")
    n = cdf["Car No."].count()
    cdf.at[n] = [carno, carname, brand, branch, fueltype, cost, category]
    cdf.to_csv("Cars.csv", index=False)
    print("Car added successfully!")


def searchCar():
    carname = input("Enter a Car name:")
    cdf = pd.read_csv("Cars.csv")
    df = cdf.loc[cdf["Car Name"] == carname]
    if df.empty:
        print("No cars found with the given code")
    else:
        print("Car details are:")
        print(df)


def deleteCar():
    carno = float(input("Enter a car number:"))
    cdf = pd.read_csv("Cars.csv")
    cdf = cdf.drop(cdf[cdf["Car No."] == carno].index)
    cdf.to_csv("Cars.csv", index=False)
    print("Car Deleted Successfully")
    print(cdf)


def showCars():
    cdf = pd.read_csv("Cars.csv")
    print(cdf)


def addNewMember():
    mid = int(input("Enter a member id:"))
    mname = input("Enter member name:")
    phoneno = int(input("Enter phone number:"))
    numberofcarsbooked = 0
    mdf = pd.read_csv("Members.csv")
    n = mdf["MID"].count()
    mdf.at[n] = [mid, mname, phoneno, numberofcarsbooked]
    mdf.to_csv("Members.csv", index=False)
    print("New Member added successfully!")
    print(mdf)


def searchMember():
    mname = input("Enter a member name:")
    mdf = pd.read_csv("Members.csv")
    df = mdf.loc[mdf["M Name"] == mname]
    if df.empty:
        print("No members found with the given name")
    else:
        print("Member details are:")
        print(df)


def deleteMember():
    mid = float(input("Enter a member id:"))
    mdf = pd.read_csv("Members.csv")
    mdf = mdf.drop(mdf[mdf["MID"] == mid].index)
    mdf.to_csv("Members.csv", index=False)
    print("Member deleted successfully")
    print(mdf)


def showMembers():
    mdf = pd.read_csv("Members.csv")
    print(mdf)


def bookCar():
    carname = input("Enter car name:")
    cdf = pd.read_csv("Cars.csv")
    cdf = cdf.loc[cdf["Car Name"] == carname]
    if cdf.empty:
        print("No Car found in the records")
        return

    mname = input("Enter member name:")
    mdf = pd.read_csv("Members.csv")
    mdf = mdf.loc[mdf["M Name"] == mname]
    if mdf.empty:
        print("No such Member found")
        return

    dateofbooking = input("Enter date of booking:")
    numberofdays = int(input("Enter the number of days booked:"))
    print("^" * 40)
    print("      BILL GENERATED   ")
    print("^" * 40)
    print("Car Rented ",carname)
    print("Name of Member ",mname)
    print("Cost per Day ",cdf["Cost"])
    total_cost = numberofdays * cdf["Cost"]
    print("Total Rental Cost ",total_cost)
    print("^" * 40)
    k = input("Press C to continue")
    bdf = pd.read_csv("Cars Booked.csv")
    n = bdf["Car Name"].count()
    bdf.at[n] = [carname, mname, dateofbooking, numberofdays,total_cost, ""]
    bdf.to_csv("Cars Booked.csv", index=False)
    print("Car booked successfully")
    print(bdf)


def returnCar():
    mname = input("Enter a member name:")
    carname = input("Enter car name:")
    rdf = pd.read_csv("Cars Booked.csv")
    rdf = rdf.loc[rdf["Car Name"] == carname]
    if rdf.empty:
        print("The car is not booked in records")
    else:
        rdf = rdf.loc[rdf["M Name"] == mname]
        if rdf.empty:
            print("The car is not booked by the member")
        else:
            print("Car can be returned")
            ans = input("Are you sure you want to return the car:")
            if ans.lower() == "yes":
                rdf = pd.read_csv("Cars Booked.csv")
                rdf = rdf.drop(rdf[rdf["Car Name"] == carname].index)
                rdf.to_csv("Cars Booked.csv", index=False)
                print("Car returned successfully")
            else:
                print("Return operation cancelled")


def showbookedCars():
    rdf = pd.read_csv("Cars Booked.csv")
    print(rdf)
    print("^" * 50)
    print("Car Name\tMember Name\tBill Amount")
    for r in rdf.iterrows():
        print(r[1]["Car Name"]+"\t"+r[1]["M Name"])
    print("^" * 50)


def deletebookedCars():
    carname = input("Enter a car name:")
    bdf = pd.read_csv("Cars Booked.csv")
    bdf = bdf.drop(bdf[bdf["Car Name"] == carname].index)
    bdf.to_csv("Cars Booked.csv", index=False)
    print("Deleted Booked cars successfully")
    print(bdf)


def showCharts():
    print("Press 1 - Cars and their Rental Cost")
    print("Press 2 - Number of Cars booked by members")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        df = pd.read_csv("Cars.csv")
        df = df[["Car Name", "Cost"]]
        df.plot("Car Name", "Cost", kind="bar")
        plt.xlabel("carname------>")
        plt.ylabel("cost------>")
        plt.show()

    if ch == 2:
        df = pd.read_csv("Cars Booked.csv")
        df = df[["No. of cars Booked", "M Name"]]
        df.plot(kind="bar", color="red")
        plt.show()


def login():
    uid = input("Enter User ID:")
    uname = input("Enter User Name:")
    pwd = input("Enter Password:")
    df = pd.read_csv("Users.csv")
    df = df.loc[df["User ID"] == uid]
    if df.empty:
        print("Invalid User ID given")
        return False
    else:
        df = df.loc[df["User Name"] == uname]
        if df.empty:
            print("Invalid User Name given")
            return False
        else:
            df = df.loc[df["Password"] == pwd]
            if df.empty:
                print("Invalid password")
                return False
            else:
                print("Username and Password matched successfully")
                return True


def showMenu():
    print("----------------------------------------------------------------------------------------")
    print("                               LUXURY CAR RENTALS                                       ")
    print("----------------------------------------------------------------------------------------")
    print("Press 1 - Add a User")
    print("Press 2 - Delete a User")
    print("Press 3 - Add a New Car")
    print("Press 4 - Search for a Car")
    print("Press 5 - Delete a Car")
    print("Press 6 - Show all Cars")
    print("Press 7 - Add a New Member")
    print("Press 8 - Search for a Member")
    print("Press 9 - Delete a Member")
    print("Press 10 - Show all Members")
    print("Press 11 - Book a Car")
    print("Press 12 - Return a Car")
    print("Press 13 - Show all Booked Cars")
    print("Press 14 - Delete a Booked Car")
    print("Press 15 - To View Charts")
    print("Press 16 - To Exit")
    choice = int(input("Enter your choice:"))
    return choice


if login():
    while True:
        ch = showMenu()
        if ch == 1:
            addUser()
        elif ch == 2:
            deleteUser()
        elif ch == 3:
            addNewCar()
        elif ch == 4:
            searchCar()
        elif ch == 5:
            deleteCar()
        elif ch == 6:
            showCars()
        elif ch == 7:
            addNewMember()
        elif ch == 8:
            searchMember()
        elif ch == 9:
            deleteMember()
        elif ch == 10:
            showMembers()
        elif ch == 11:
            bookCar()
        elif ch == 12:
            returnCar()
        elif ch == 13:
            showbookedCars()
        elif ch == 14:
            deletebookedCars()
        elif ch == 15:
            showCharts()
        elif ch == 16:
            break
        else:
            print("Invalid Option Selected")
print("THANK YOU FOR VISITING LUXURY CAR RENTALS")









