import mysql.connector
import random
file=mysql.connector.connect(host="localhost" ,user="root", passwd="vaanipop" , database="myshop")
from datetime import datetime
available=["BEVERAGES" ,"DAALS_AND_OTHERS","DAIRY","FRUITS","SOAPS_AND_OTHERS","SPICES","VEGETABLES"]
maximum=0
sum=0
price=0
plum=0
f=file.cursor()
def menu():
    f.execute("select ITEM_NAME,PRICE from BEVERAGES")
    DATA=f.fetchall()
    print(DATA)
    f.execute("select ITEM_NAME,PRICE from DAALS_AND_OTHERS")
    D=f.fetchall()
    print(D)
    f.execute("select ITEM_NAME,PRICE from DAIRY")
    A=f.fetchall()
    print(A)
    f.execute("select ITEM_NAME,PRICE from FRUITS")
    T=f.fetchall()
    print(T)
    f.execute("select ITEM_NAME,PRICE from VEGETABLES")
    V=f.fetchall()
    print(V)
    f.execute("select ITEM_NAME,PRICE from SOAPS_AND_OTHERS")
    F=f.fetchall()
    print(F)
    f.execute("select ITEM_NAME,PRICE from SPICES")
    S=f.fetchall()
    print(S)
def track(entered):
    f.execute("select STATUS_OF_ORDER from ORDERS where ORDER_ID='{}' ".format(entered))
    doooon =f.fetchall()
    print(doooon)
def orders(a,b):
    f.execute("select*from orders where phone_no='{}' and full_name='{}' ".format(a,b))
    dam=f.fetchall()
    print(dam)
    x=10
    while x==10:
        num=int(input("To see what all you ordered in these orders ,enter the order id you want to access(enter 0 to exit)"))
        if num==0:
            x=0
        else:
            f.execute("select order_item , quantity from orders_item1 where order_id='{}' ".format(num))
            helpo=f.fetchall()
            print(helpo)

print("Hello , welcome to MYSHOP")
name=input("Enter your  FULL NAME")
name=name.upper()
block=90
neon=0
length=0
while block==90:
    phone=int(input("Enter your phone number"))
    phone2=phone
    while phone >1:
       phone=phone/10
       neon=neon+1
    length=neon
    if length==10:
        block=80
    else:
        print("Please enter a valid number")
    neon=0
phone=phone2

l=[]
b=int(input("So ,What would you like to do?  1.View our Menu (enter 1)  2.Order grocery(enter 2) 3.Track your order(enter 3)  4.View your previous orders(enter 4)"))
if b==1:
    menu()
elif b==2:
    now= datetime.now()

    current_time = now.strftime("%H:%M:%S")

    date_= datetime.today().strftime('%Y-%m-%d')
    address=input("enter your address")
    mun=7
    while mun==7:
        payment=input("Enter your mode of payment ie a) Netbanking or b)Cash on delivery")
        if payment=="a":
           payment="NET BANKING"
           mun=10
           pass


        elif payment=="b":
           payment="CASH ON DELIVERY"
           mun=10
           pass
        else:
           print("Please enter valid character")


    f.execute("Select ORDER_ID from ORDERS")
    font=f.fetchall()
    for i in font:
        l.append(i[0])
    n=0
    var=0
    while n==0:
        a=random.randint(0,10000000000)
        for i in l:
            if i==a:
                 b+=1
            else:
                pass

        if var>0:
            n=0
        else:
             n=10
    order_id=a
    print("your order id is",order_id)
    #for orders:
    orde=10
    while orde==10:
        pack=input("Enter what would you like to order(ENTER 0 EXIT)")
        if pack=="0":
            orde=4
        else:
            pack=pack.upper()
            quantity=int(input("Enter the quantity you would like to order"))
            if quantity==0:
                print("The quantity uyou entered is zero")
            else:
               f.execute("Insert into orders_item1 (ORDER_ID, ORDER_ITEM ,QUANTITY) values ({},'{}',{} )".format(order_id,pack,quantity))
               file.commit()
               for i in available:
                f.execute("Select item_name from {} ".format(i))
                hall=f.fetchall()
                for j in hall:
                    if j[0]==pack:
                        f.execute("Select PRICE from {} where item_name='{}'".format(i,pack))
                        ANDO=f.fetchall()
                        for k in ANDO:
                            sum=k[0]
                            price=price+quantity*sum
                        f.execute("Select DAYS_NEEDED_FOR_DELIVERY from {} where item_name='{}'".format(i,pack))
                        call=f.fetchall()
                        for v in call:
                            plum=v[0]
                            if plum>maximum:
                                maximum=plum
                                print(maximum)
                            else:
                                pass
                    else:
                        pass
    print("The amount you need to pay is",price)
    print("The maximum days needed for delivery are",maximum)
    f.execute("Insert into orders(ORDER_ID ,FULL_NAME,PHONE_NO,ADDRESS,MODE_OF_PAYMENT,STATUS_OF_ORDER,DATE_OF_ORDER_IN_YYYYMMDD,TIME_)values({},'{}',{},'{}','{}','{}','{}','{}')".format(order_id,name,phone ,address,payment,"not yet started",date_,current_time))
    file.commit()
elif b==3:
    entered=int(input("Enter your order id"))
    track(entered) #define the function track
elif b==4:
    print("showing your previous orders")
    orders(phone,name)# define the function orders
else:
    print("Unidentified character entered")
file.close()
