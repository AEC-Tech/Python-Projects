import pandas as pd
import matplotlib.pyplot as plt
import random


def addSweet(df):
    code = int(input("Enter the sweet code "))
    name = input("Enter the name of the sweet ")
    cost = int(input("Enter cost per kg "))
    qty = float(input("Enter quantity in kgs "))
    ig = input("Enter the main ingredient ")
    df.loc[code] = [name, cost, qty, ig]
    print("\nAdded Successfully \n")


print("*"*50)
print("\t\t Kanha Sweet Shop")
print("*"*50)
df = pd.read_csv("sweets.csv")

while True:
    print("Press 1 - Add a New Sweet")
    print("Press 2 - Show all")
    print("Press 3 - Search")
    print("Press 4 - Delete")
    print("Press 5 - Update")
    print("Press 6 - Create Bill")
    print("Press 7 - Show Chart of Sweets")
    print("Press 8 - Show Chart of Bills")
    print("Press 9 - To Quit")
    n = int(input("Enter your choice : "))
    if n == 1:
        addSweet(df)
    elif n == 2:
        print("\n","*"*50)
        print(df)
        print("*"*50)
    elif n == 3:
        code = int(input("Enter the sweet code to be searched : "))
        if code in df.index:
            print(df.loc[code])
            print("\n")
        else:
            print("No sweet found with this code ")
    elif n == 4:
        code = int(input("Enter the sweet code to be deleted : "))
        if code in df.index:
            df.drop(code,inplace=True)
            print("\nDeleted\n")
        else:
            print("No sweet found with this code ")
    elif n == 5:
        code = int(input("Enter the sweet code to be updated : "))
        if code in df.index:
            name = input("Enter the updated name of the sweet ")
            cost = int(input("Enter updated cost per kg "))
            qty = float(input("Enter quantity in kgs "))
            ig = input("Enter the main ingredient ")
            df.loc[code] = [name, cost,qty,ig]
            print("\nUpdated\n")
        else:
            print("No sweet found with this code ")
    elif n == 6:
        print("Available Sweets ")
        print("\n", "*" * 50)
        print(df)
        print("*" * 50)
        code = int(input("Enter the code of the sweet to be purchased : "))
        if code in df.index:
            qty = int(input("Enter the quantity to be purchased : "))
            amt = qty * df.loc[code,"Cost"]
            print("Your Due Amount is ",amt)
            name = input("Enter Customer name : ")
            bdate = input("Enter Billing Date : ")
            bf = pd.read_csv("customer.csv",index_col="billid")
            bf.loc[random.randint(1000,9999)] = [name,bdate,amt,df.loc[code,"Name"]]
            bf.to_csv("customer.csv")
        else:
            print("No sweet found with this code ")
    elif n == 7:
        plt.bar(df["Name"],df["Cost"],color="navy")
        plt.title("Rate List of Sweets")
        plt.show()
    elif n == 8:
        bf = pd.read_csv("customer.csv")

        plt.title("Sold Sweets")
        plt.bar(bf["name"],bf["order_amt"],color="orange")
        plt.show()
    elif n == 9:
        df.to_csv("sweets.csv",index=False)
        print("Thanks for Visiting")
        print("Data Updated !!!")
        break

