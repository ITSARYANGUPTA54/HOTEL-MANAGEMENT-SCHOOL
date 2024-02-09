import mysql.connector as mycon
con = mycon.connect(host="localhost",user="root",password="aryangupta123")
def connect():    
    c1=con.cursor()
    c1.execute("create database HOTELS287")
    c1.execute("use HOTELS287")
    c1.execute("create table rooms(romm_no integer,type varchar(50),no_of_guest integer,rent integer, status varchar(20))")
    c1.execute("create table billing(cname varchar(20),idtype varchar(40),idno varchar(40), address varchar(50), phone varchar(10),gender varchar(20),dcheckin date,room_no integer)")
    c1.execute("create table booking(cname varchar(30),idno varchar(15),idtype varchar(30),address varchar(30),phone varchar(30),gender varchar(30),dateofcheckin varchar(30),room_no varchar(20))")
    c1.execute("create table resturant(s varchar(20),nat varchar(20),food varchar(20),cost varchar(10))")
    c1.execute("create table laundary(s varchar(20),item varchar(20),cost varchar(20))")
    con.commit()
    
    
    ch=int(input("ENTER THE NUMBER OF RECORDS TO BE ENTERED FOR LAUNDARY SERVICE "))
    
    for i in range(0,ch):
            s=input("ENTER THE S.NO ")
            item=input("ENTER THE ITEM NAME ")
            cost=input("ENTER IT'S PRICE ")
            st="insert into laundary VALUES(%s,%s,%s)"
            val=(s,item,cost)
            c1.execute(st,val)
            con.commit()
def laundry():
    print("DO YOU WANT TO SEE RATE FOR LAUNDRY?")
    ch=int(input("If yes press 1 "))
    if ch==1:
        c1=con.cursor()
        sql="select * from laundary"
        c1.execute(sql)
        rows=c1.fetchall()
        for x in rows:
            print(x)

            
def laundrybill():
    c1=con.cursor()
    sql="select * from laundary"
    c1.execute(sql)
    rows=c1.fetchall()
    for x in rows:
        print(x)
    s=0
    l='y'
    n=0
    while l=='y':
        ch=int(input("Enter your choice"))
        if ch==1:
            print("YOU HAVE OPTED FOR PANT WASH,COST is 10rs")
            n=int(input("Enter no. of pants "))
            s=s+(10*n)
        elif ch==2:
            print("YOU HAVE OPTED FOR SHIRT WASH,COST is 12rs")
            n=int(input("Enter no. of shirts "))
            s=s+(12*n)
        elif ch==3:
            print("YOU HAVE OPTED FOR SUIT WASH,COST is 30rs")
            n=int(input("Enter no. of suits "))
            s=s+(30*n)
        elif ch==4:
            print("YOU HAVE OPTED FOR SARI WASH,COST is 20rs")
            n=int(input("Enter no. of saris "))
            s=s+(20*n)
        elif ch==5:
            print("YOU HAVE OPTED FOR DRESS(women) WASH,COST IS 20rs")
            n=int(input("Enter no. of dresses "))
            s=s+(20*n)
        l=input("DO YOU WANT TO GIVE MORE CLOTHES FOR LAUNDRY")
        if (l not in 'y'):
            print("TOTAL AMOUNT IS",s)

    
def resturantmenuview():
    print("DO YOU WANT TO ORDER THALI OR INDEPENDENTLY?")
    print("1.THALI")
    print("2.CHOICE ORDER ")
    ch=int(input(" "))
    if ch==1:
         print("###### MENU OF 500 RS. PER PLATE #######")
         print("1.RICE")
         print("2.CHAPATI (ROTI AND NAAN)")
         print("3. DAL MAKHNI")
         print("4.MIX VEGETABLE")
         print("5.GULAB JAMUN")
         print("\n"*2)

         print("###### MENU OF RS. 800 PER PLATE #######")
         print("1.RICE")
         print("2.CHAPATI(ROTI,NAAN,BUTTER NAAN)")
         print("3. DAL MAKHNI")
         print("4.MIX VEGETABLE")
         print("5. PANEER CURRY")
         print("6.PAPAD")
         print("7.GULAB JAMUN")

         print("\n"*2)
         print("###### MENU OF RS. 1000 PER PLATE#######")
         print("1.RICE")
         print("2.CHAPATI(ROTI,BUTTER NAAN,RUMALI ROTI)")
         print("3.DAL MAKHNI")
         print("4.MIX VEGETABLE")
         print("5.PANEER CURRY")
         print("6.PAPAD")
         print("7.ICE CREAM & GULAB JAMUN")
         print("8.CHOWMIEN & BURGER")

         print("\n"*2)
         print("###### MENU OF RS. 1200 PER PLATE#######")
         print("1.RICE/FRIED RICE")
         print("2.CHAPATI(ROTI,NAAN,BUTTER NAAN,RUMALI ROTI)")
         print("3.DAL  MAKHNI & CHOLE/RAJMA")
         print("4.MIX VEGETABLE")
         print("5.ONE PANEER CURRY")
         print("6.PAPAD")
         print("7.GULAB JAMUN & ICE CREAM")
         print("8.CHOWMIEN, BURGER,PIZZA,SPRING ROLL")
         print("\n"*2)

         print("###### MENU OF RS. 1500 PER PLATE#######")
         print("1.RICE/FRIED RICE/PASTA")
         print("2.CHAPATI(ROTI,BUTTER NAAN,RUMALI ROTI,KASHMIRI ROTI)/PURI")
         print("3.DAL  MAKHNI , CHOLE/RAJMA & CURD")
         print("4.MIX VEGETABLE")
         print("5.PANEER PASANDA & PANEER CHILLY")
         print("6.PAPAD/ACHAR")
         print("7.GULAB JAMUN,ICE CREAM,MOONG DAL HALWA")
         print("8.CHOWMIEN,BURGER,PIZZA,SPRING ROLL")
         print("\n"*2)
         ch=int(input("ENTER YOUR CHOICE"))
         if ch==1:
             print("YOU HAVE SELECTED 500\\- PLATE")
             n=int(input("AMOUNT:- "))
             print("Your total is",500*n)
             print("THANKS!")
         if ch==2:
             print("YOU HAVE SELECTED 800\\- PLATE")
             n=int(input("AMOUNT:- "))
             print("Your total is",800*n) 
             print("THANKS!")
         if ch==3:
             print("YOU HAVE SELECTED 1000\\- PLATE")
             n=int(input("AMOUNT:- "))
             print("Your total is",1000*n) 
             print("THANKS!")
         if ch==4:
             print("YOU HAVE SELECTED 1200\\- PLATE")
             n=int(input("AMOUNT:- "))
             print("Your total is",1200*n) 
             print("THANKS!")
         if ch==5:
             print("YOU HAVE SELECTED 1500\\- PLATE")
             n=int(input("AMOUNT:- "))
             print("Your total is",1500*n) 
             print("THANKS!")
    elif ch==2:
       
       print("ENTER 1 TO SEE MENU")
       ch=int(input(""))
       print("S.no cusine item rate") 
       if ch==1:
           print(" 1:- chole bathure-------cost is 100rs")
           print(" 2:- dosa sambhar--------cost is 100rs")
           print(" 3:- kachori-------------cost is 50rs")
           print(" 4:- litti chokha--------cost is 150rs")
           print(" 5:- dal batti-----------cost is 150rs")
           print(" 6:- chicken tikka-------cost is 250rs")
           print(" 7:- rogan josh----------cost is 300rs")
           print(" 8:- kebabs--------------cost is 150rs")
           print(" 9:- samosa--------------cost is 50rs")
           print(" 10:- vada pav-----------cost is 50rs")
           print(" 11:- thukpa-------------cost is 200rs")
           print(" 12:- dahi balla---------cost is 150rs")
           print(" 13:- khandvi------------cost is 200rs")
       l='y'
       s=0
       while l=='y':
           ch=int(input("ENTER YOUR CHOICE "))
           if ch==1:
               print("You have ordered chole bathure, cost is 100rs")
               a=int(input("Please enter how many plates?"))
               s=s+(100*a)
           elif ch==2:
               print("You have ordered dosa sambhar, cost is 100rs")
               a=int(input("Please enter how many plates?"))
               s=s+(100*a)
           elif ch==3:
                print("You have ordered kachori, cost is 50rs")
                a=int(input("Please enter how many?"))
                s=s+(50*a)
           elif ch==4:
               print("You have ordered litti chokha, cost is 150rs")
               a=int(input("Please enter how many plates? "))
               s=s+(150*a)
           elif ch==5:
               print("You have ordered dal batti,cost is 150rs")
               a=int(input("Please enter how many plates? "))
               s=s+(150*a)
           elif ch==6:
              print("You have ordered chicken tikka, cost is 250rs")
              a=int(input("Please enter how many plates?"))
              s=s+(250*a)
           elif ch==7:
              print("You have ordered rogan josh, cost is 300rs")
              a=int(input("Please enter how many plates?"))
              s=s+(300*a)
           elif ch==8:
               print("You have ordered kebabs, cost is 150rs")
               a=int(input("Please enter how many plates?"))
               s=s+(150*a)
           elif ch==9:
               print("You have ordered samosa, cost is 50rs")
               a=int(input("Please enter how many?"))
               s=s+(50*a)
           elif ch==10:
               print("You have ordered vada pav, cost is 50rs")
               a=int(input("Please enter how many?"))
               s=s+(50*a)
           elif ch==11:
                print("You have ordered thukpa, cost is 200rs")
                a=int(input("Please enter how many bowls?"))
                s=s+(200*a)
           elif ch==12:
               print("You have ordered dahi balla, cost is 150rs")
               a=int(input("Please enter how many plates?"))
               s=s+(150*a)
           elif ch==13:
               print("You have ordered khandvi, cost is 200rs")
               a=int(input("Please enter how many plates?"))
               s=s+(200*a)
           elif ch==14:
               print("You have ordered idiyappam, cost is 400rs")
               a=int(input("Please enter how many plates?"))
               s=s+(400*a)
           elif ch==15:
              print("You have ordered utapam, cost is 80rs")
              a=int(input("Please enter how many?"))
              s=s+(80*a)
           elif ch==16:
               print("You have ordered dumplings, cost is 150rs")
               a=int(input("Please enter how many plates? "))
               s=s+(150*a)
           elif ch==17:
               print("You have ordered chowmien, cost is 150rs")
               a=int(input("Please enter how many plates? "))
               s=s+(150*a)
           elif ch==18:
               print("You have ordered hotpot , cost is 450rs")
               a=int(input("Please enter how many pots? "))
               s=s+(450*a)
           elif ch==19:
              print("You have ordered pasta, cost is 250rs")
              a=int(input("Please enter how many plates?"))
              s=s+(250*a)
           elif ch==20:
               print("You have ordered pizza, cost is 250rs")
               a=int(input("Please enter how many?"))
               s=s+(250*a)
           elif ch==21:
               print("You have ordered biryani, cost is 500rs")
               a=int(input("Please enter how many plates?"))
               s=s+(500*a)
           elif ch==22:
               print("You have ordered shahi tukda, cost is 350rs")
               a=int(input("Please enter how many plates?"))
               s=s+(350*a)
           elif ch==23:
              print("You have ordered tacos,cost is 275rs")
              a=int(input("Please enter how many plates?"))
              s=s+(275*a)
           elif ch==24:
              print("You have ordered tomato salsa, cost is 300rs")
              a=int(input("Please enter how many plates?"))
              s=s+(300*a)
           elif ch==25:
              print("You have ordered salad, cost is 300rs")
              a=int(input("Please enter how many plates?"))
              s=s+(300*a)
           l=input("Do you want to order more y/n")
           if(l not in 'y'):
               print("Total Amount=",s)



def showmenu():
    while True:
        print("#" * 30)
        print("----    HOTEL PANORAMA    ----")
        print("#" * 30)
        print("Press 1 - Create a New Room")
        print("Press 2 - Show All Rooms")
        print("Press 3 - Show All Vacant Rooms")
        print("Press 4 - Show All Occupied Rooms")
        print("Press 5 - Book a Room")
        print("Press 6 - Check Out")
        print("Press 7 - for ordering food")
        print("Press 8 - laundary")
        print("press 9 - laundary bills")
        print("Press 10 - Exit")
        
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
            resturantmenuview()
        elif choice == 8:
            laundry()
        elif choice == 9:
            laundrybill()
        elif choice == 10:            
             break
        
            
def createRoom():
    print(" --- ENTER ROOM DETAILS  --- ")
    rno = int(input("Enter Room No. : "))
    type = input("Enter Room Type(Simple/Delux/Super Delux):")
    guest = int(input("Enter maximum number of guests : "))
    rent = int(input("Enter Per Day Charges : "))
    status = "Vacant"
    q = "insert into rooms values(%s,%s,%s,%s,%s)"
    data = (rno,type,guest,rent,status)
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
    connect()
    showmenu()

