from tkinter import *
import mysql.connector as m

try:
    #CONNECTING WITH MYSQL AND MAKING A CURSOR
    connection = m.connect(host='localhost',user='root', passwd='root')
    cur = connection.cursor()

    #CREATING DATABASE AND TABLE IF NOT PRESENT IN THE SYSTEM
    query = "create database if not exists mobile"
    cur.execute(query)
    query = 'use mobile'
    cur.execute(query)
    query='''create table if not exists phone(
    name varchar(60) primary key , 
    phone_no varchar(20) unique, 
    address varchar(100))'''
    cur.execute(query)

    # CREATING THE MAIN TKINTER WINDOW OF CONTACT BOOK
    win = Tk()
    win.title("CONTACT BOOK")
    win.geometry("630x300")
    entrance = Label(win, text="WELCOME TO THE CONTACT BOOK", font=("Comic sans ms", 25, "bold"), bg='black',fg='yellow').place(x=10, y=40)

    #FUNCTION FOR THE OPERATIONS DONE IN CONTACT BOOK

    def tki_showcontact():
        '''FUNCTION TO SHOW ALL CONTACTS OF THE CONTACT BOOK'''
        win1 = Tk()
        win1.title("ALL CONTACTS IN THE CONTACT BOOK")

        query = "select * from phone order by name"
        cur.execute(query)
        data = cur.fetchall()
        a = 1
        if len(data) == 0:
            l1 = Label(win1, text="YOU DON'T HAVE ANY CONTACT SAVED !!!", font=("Comic sans ms", 15, 'bold'), bg='cyan',fg='BLACK').grid(row=a, column=1)
            l2 = Label(win1, text="PLEASE SAVE SOME CONTACT FIRST", font=("Comic sans ms", 15, 'bold'), bg='cyan',fg='BLACK').grid(row=a + 1, column=1)


        else:
            l1 = Label(win1, text="NAME  ", font=("Comic sans ms", 15, 'bold'), bg='yellow', fg='BLACK').grid(row=a,column=1)
            l2 = Label(win1, text="  PHONE NO.  ", font=("Comic sans ms", 15, 'bold'), bg='yellow', fg='BLACK').grid(row=a, column=4)
            l3 = Label(win1, text="  ADDRESS  ", font=("Comic sans ms", 15, 'bold'), bg='yellow', fg='BLACK').grid(row=a, column=7)
            for i in data:
                a += 1
                Label(win1, text=i[0], font=("Comic sans ms", 15, 'bold'), bg='cyan', fg='BLACK').grid(row=a, column=1)
                l5 = Label(win1, text=i[1], font=("Comic sans ms", 15, 'bold'), bg='cyan', fg='BLACK').grid(row=a,column=4)
                l6 = Label(win1, text=i[2], font=("Comic sans ms", 15, 'bold'), bg='cyan', fg='BLACK').grid(row=a,column=7)

        ext = Button(win1, text="Exit", font=("Comic sans ms", 10, 'bold'), bg='green', fg='YELLOW',command=win1.destroy).grid(row=a + 4, column=1)

        win1.mainloop()

    def tki_addcontact():
        '''FUNCTION TO ADD A NEW CONTACT IN THE CONTACT BOOK'''
        win2 = Tk()
        win2.title("ADDING A CONTACT")
        win2.geometry("552x300")
        l = Label(win2, text="PLEASE FILL CONTACT DETAILS", font=("Comic sans ms", 15, 'bold'), bg='GREY', fg='BLACK').place(x=104,y=5)

        l1 = Label(win2, text="Enter person name:-", font=("Comic sans ms", 15, 'bold'), bg='cyan', fg='blue').place(x=20,y=60)
        t1 = Entry(win2, font=("Comic sans ms", 10), bg='white', fg='black')
        t1.place(x=260, y=66)

        l2 = Label(win2, text="Enter phone number:-", font=("Comic sans ms", 15, 'bold'), bg='cyan', fg='blue').place(x=20,y=100)
        t2 = Entry(win2, font=("Comic sans ms", 10), bg='white', fg='black')
        t2.place(x=260, y=106)

        l3 = Label(win2, text="Enter address :-", font=("Comic sans ms", 15, 'bold'), bg='cyan',fg='blue').place(x=20, y=140)
        t3 = Entry(win2, font=("Comic sans ms", 10), bg='white', fg='black')
        t3.place(x=260, y=146)

        def addcontact():
            name = t1.get().strip()
            phn_no = t2.get()
            address = t3.get()
            s = "select * from phone where name='" + name + "' or phone_no='"+phn_no+"'"
            cur.execute(s)
            data = cur.fetchall()
            if len(data)==0:
                if len(phn_no)==10:
                    query = "insert into phone values('%s','%s','%s')" % (name, phn_no, address,)
                    cur.execute(query)
                    connection.commit()
                    res = Label(win2, text="DETAILS OF "+name+" ADDED SUCCESSFULLY                       ", font=("Comic sans ms", 15, 'bold'), ).place(x=10,y=230)
                else:
                    res = Label(win2, text="PHONE NUMBER INVALID !!!                           ",font=("Comic sans ms", 15, 'bold'), ).place(x=10, y=230)
            else:
                res = Label(win2, text="CAN'T HAVE DUPLICATE NAME OR PHONE NUBMER        ",font=("Comic sans ms", 15, 'bold'), ).place(x=10, y=230)

        sub1 = Button(win2, text="SUBMIT", font=("Comic sans ms", 10, 'bold'), bg='BLACK', fg='YELLOW',command=addcontact).place(x=165, y=190)
        sub2 = Button(win2, text="EXIT", font=("Comic sans ms", 10, 'bold'), bg='BLACK', fg='YELLOW',command=win2.destroy).place(x=325, y=190)

    def tki_searchcontact():
        '''FUNCTION TO SEARCH A CONTACT IN THE CONTACT BOOK'''
        win3 = Tk()
        win3.geometry("520x300")
        win3.title("SEARCHING A CONTACT ")

        l = Label(win3, text="SEARCH CONTACT", font=("Comic sans ms", 15, 'bold'), bg='YELLOW', fg='RED').place(x=170, y=5)
        l1 = Label(win3, text="Enter person name:-", font=("Comic sans ms", 15, 'bold'), bg='ORANGE', fg='BLACK').place(x=20,y=70)
        t1 = Entry(win3, font=("Comic sans ms", 10), bg='WHITE', fg='BLACK')
        t1.place(x=240, y=80)


        def searchcontact():
            n=t1.get()
            query = "select * from phone where name='"+n+"'"
            cur.execute(query)

            data = cur.fetchone()
            if data==None:
                W = Label(win3, text="NO CONTACT FOUND !!!!", font=("Comic sans ms", 15, 'bold'), bg='ORANGE', fg='BLACK').place(x=10,y=180)
                W1 = Label(win3, text=" "*500+"\n"+" "*500).place(x=10,y=220)
                W2 = Label(win3, text=" "*500+"\n"+" "*500).place(x=10,y=260)

            else:
                W = Label(win3, text=" "*35).place(x=10,y=180)
                W1 = Label(win3, text="NAME:-"+data[0]+"                                      ", font=("Comic sans ms", 15, 'bold'), fg='BLACK').place(x=10,y=180)
                W2 = Label(win3, text="PHONE NO.:-"+data[1], font=("Comic sans ms", 15, 'bold'),  fg='BLACK').place(x=10,y=220)
                W3 = Label(win3, text="ADDRESS:-"+data[2], font=("Comic sans ms", 15, 'bold'), fg='BLACK').place(x=10,y=260)


        but1 = Button(win3, text="SEARCH", font=("Comic sans ms", 10, 'bold'), bg='green', fg='YELLOW',command=searchcontact).place(x=150, y=120)
        but2 = Button(win3, text="Exit", font=("Comic sans ms", 10, 'bold'), bg='green', fg='YELLOW',command=win3.destroy).place(x=240, y=120)

    def tki_modcontact():
        '''FUNCTION TO MODIFY A CONTACT IN THE CONTACT BOOK'''
        win4 = Tk()
        win4.title("MODIFY CONTACT ")
        win4.geometry("700x250")

        l = Label(win4, text="MODIFY CONTACT", font=("Comic sans ms", 15, 'bold'), bg='YELLOW', fg='black').place(x=260,y=5)

        def modifynumber():
            '''FUNCTION FOR MODIFYING NUMBER'''
            l1 = Label(win4, text="Enter person name to update its contact:-", font=("Comic sans ms", 15, 'bold'),bg='ORANGE', fg='BLACK').place(x=37, y=90)
            t1 = Entry(win4, font=("Comic sans ms", 10), bg='white', fg='black')
            t1.place(x=490, y=96)

            l2 = Label(win4, text=" Enter new phone number:-", font=("Comic sans ms", 15, 'bold'), bg='ORANGE',fg='BLACK').place(x=108, y=130)
            t2 = Entry(win4, font=("Comic sans ms", 10), bg='white', fg='black')
            t2.place(x=490, y=136)

            def modifycontact():
                n = t1.get().strip()
                p = t2.get()
                s = "select * from phone where name='" + n + "'"
                cur.execute(s)
                data = cur.fetchall()
                if len(data) != 0:
                    if len(p)==10:
                        check = "select * from phone where phone_no='" + p + "'"
                        cur.execute(check)
                        data1 = cur.fetchall()
                        if len(data1)==0:
                            query = "update phone set phone_no='%s' where name='%s'" % (p, n,)
                            cur.execute(query)
                            connection.commit()
                            res = Label(win4, text="DETAILS OF " + n + " UPDATED SUCCESSFULLY                  ", font=("Comic sans ms", 15, 'bold'), ).place(x=10, y=210)
                        else:
                            res = Label(win4, text="THIS PHONE NUMBER ALREADY SAVED !!!                       ",font=("Comic sans ms", 15, 'bold'), ).place(x=10, y=210)
                    else:
                        res = Label(win4, text="INVALID PHONE NUMBER !!!                                 ",font=("Comic sans ms", 15, 'bold'), ).place(x=10, y=210)
                else:
                    res = Label(win4, text=n+" NAMED CONTACT DOESN'T EXISTS                            ",font=("Comic sans ms", 15, 'bold'), ).place(x=10, y=210)

            sub1 = Button(win4, text="Modify", font=("Comic sans ms", 10, 'bold'), bg='green', fg='YELLOW',command=modifycontact).place(x=270, y=170)
            sub2 = Button(win4, text="Exit", font=("Comic sans ms", 10, 'bold'), bg='green', fg='YELLOW',command=win4.destroy).place(x=400, y=170)

        def modifyaddress():
            '''FUNCTION FOR MODIFYING NADDRESS'''
            l1 = Label(win4, text="Enter person name to update its contact:-", font=("Comic sans ms", 15, 'bold'),bg='ORANGE', fg='BLACK').place(x=37, y=90)
            t1 = Entry(win4, font=("Comic sans ms", 10), bg='white', fg='black')
            t1.place(x=490, y=96)

            l2 = Label(win4, text="    Enter new address:-    ", font=("Comic sans ms", 15, 'bold'), bg='ORANGE',fg='BLACK').place(x=108, y=130)
            t2 = Entry(win4, font=("Comic sans ms", 10), bg='white', fg='black')
            t2.place(x=490, y=136)

            def modifycontact():
                n = t1.get()
                a = t2.get()
                s = "select * from phone where name='" + n + "'"
                cur.execute(s)
                data = cur.fetchall()
                if len(data) != 0:
                    query = "update phone set address='%s' where name='%s'" % (a, n,)
                    cur.execute(query)
                    connection.commit()
                    res = Label(win4, text="DETAILS OF " + n + "UPDATED SUCCESSFULLY                ",font=("Comic sans ms", 15, 'bold'), ).place(x=10, y=210)
                else:
                    res = Label(win4, text=n+" NAMED CONTACT DOESN'T EXISTS                   ",font=("Comic sans ms", 15, 'bold'), ).place(x=10, y=210)


            sub1 = Button(win4, text="Modify", font=("Comic sans ms", 10, 'bold'), bg='green', fg='YELLOW',command=modifycontact).place(x=270, y=170)
            sub2 = Button(win4, text="Exit", font=("Comic sans ms", 10, 'bold'), bg='green', fg='YELLOW',command=win4.destroy).place(x=400, y=170)

        sub1 = Button(win4, text="Modify Number", font=("Comic sans ms", 10, 'bold'), bg='green', fg='YELLOW',command=modifynumber).place(x=190, y=50)
        sub2 = Button(win4, text="Modify Address", font=("Comic sans ms", 10, 'bold'), bg='green', fg='YELLOW',command=modifyaddress).place(x=320, y=50)
        sub3 = Button(win4, text="Exit", font=("Comic sans ms", 10, 'bold'), bg='green', fg='YELLOW',command=win4.destroy).place(x=450, y=50)

    def tki_delcontact():
        '''FUNCTION TO DELETE A CONTACT IN THE CONTACT BOOK'''
        win5=Tk()
        win5.title("DELETE CONTACT ")
        win5.geometry("430x200")

        l = Label(win5, text="DELETION", font=("Comic sans ms", 15, 'bold'), bg='GREY',fg='BLACK').place(x=170, y=5)
        l1 = Label(win5, text="Enter person name:-", font=("Comic sans ms", 15, 'bold'), bg='cyan', fg='blue').place(x=20,y=70)
        t1 = Entry(win5, font=("Comic sans ms", 10), bg='white', fg='black')
        t1.place(x=240, y=80)

        def delcontact():
            a = t1.get().strip()
            s="select * from phone where name='"+a+"'"
            cur.execute(s)
            data=cur.fetchall()
            if len(data)!=0:
                query = "delete from phone where name='" + str(a) + "'"
                cur.execute(query)
                connection.commit()
                res = Label(win5, text="DETAILS OF "+a+" DELETED SUCCESSFULLY", font=("Comic sans ms", 10, 'bold'), ).place(x=10,y=160)
            else:
                res = Label(win5, text="NO CONTACT FOUND WITH THIS NAME",font=("Comic sans ms", 10, 'bold'), ).place(x=10, y=160)

        sub1 = Button(win5, text="Delete", font=("Comic sans ms", 10, 'bold'), bg='green', fg='YELLOW',command=delcontact).place(x=150, y=120)
        sub2 = Button(win5, text="Exit", font=("Comic sans ms", 10, 'bold'), bg='green', fg='YELLOW',command=win5.destroy).place(x=240, y=120)

    def exiting_code():
        '''FUNCTION TO EXIT THE CONTACT BOOK'''
        win.destroy()


    #BUTTONS ON THE MAIN SCREEN
    b1 = Button(win, text="SHOW CONTACT", font=("Comic sans ms", 10, "bold"), bg='CYAN', fg='BLACK',command=tki_showcontact).place(x=134, y=100)
    b2 = Button(win, text="ADD CONTACT", font=("Comic sans ms", 10, "bold"),bg='CYAN', fg='BLACK',command=tki_addcontact).place(x=350, y=100)
    b3 = Button(win, text="SEARCH CONTACT", font=("Comic sans ms", 10, "bold"),bg='CYAN', fg='BLACK',command=tki_searchcontact).place(x=130, y=150)
    b4 = Button(win, text="MODIFY COTNACT", font=("Comic sans ms", 10, "bold"), bg='CYAN', fg='BLACK',command=tki_modcontact).place(x=340,y=150)
    b5 = Button(win, text="DELETE CONTACT ", font=("Comic sans ms", 10, "bold"),bg='CYAN', fg='BLACK',command=tki_delcontact ).place(x=130,y=200)
    b6 = Button(win, text="EXIT", font=("Comic sans ms", 10, "bold"),bg='CYAN', fg='BLACK',command=exiting_code ).place(x=374,y=200)

    win.mainloop()

except:
    #IF ERROR COMES IN CONNECTING WITH DATABASE THE CODE BELOW WILL EXECUTE
    win6 = Tk()
    win6.title("ERROR ")
    win6.geometry("440x100")
    res = Label(win6, text="UNABLE TO CONNECT WITH MYSQL", bg='YELLOW', fg='BLACK',font=("Comic sans ms", 16, 'bold'), ).place(x=10, y=10)
    b6 = Button(win6, text="EXIT", font=("Comic sans ms", 10, "bold"), bg='CYAN', fg='BLACK',command=win6.destroy).place(x=200, y=70)
    win6.mainloop()
