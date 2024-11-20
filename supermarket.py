from  datetime import datetime

name=input("enter your name:")
lists='''
Rice    rs 60/kg
sugar   Rs 30/kg
oil     Rs 100/1L
magii   Rs 10/1p
salt    Rs 10/1p
boost   Rs 5/1p
hair oil RS 120/1L
colgate Rs 130/1kg
'''
price=0
pricelist=[]
totalprice=0
finalprice=0
qlist=[]
plist=[]
ilist=[]
items={"Rice":60,
"sugar":30,
"oil":100,
"maggi":10,
"salt":10,
"boost":5,
"hair oil":120,
"colgate":130}
option=int(input("for your want item list press 1:"))  
if option==1:
    print(lists) 
for reddy in range(len(items)):
    reddy=int(input("if you want buy press 1 you don't want press 2:"))
    if reddy==2:
        break
    if reddy==1:
        item=input("enter you item:")
        quntity=int(input("enter you quntity:"))
        if item in items.keys():
            price=quntity*(items[item])
            pricelist.append((item,quntity,items,price))
            totalprice+=price
            qlist.append(quntity)
            ilist.append(item)
            plist.append(item)
            gst=(totalprice*5)/100
            finalamount=(gst+totalprice)
        else:
            print("sorry your item not there in market")
    else:
        print("you enter worge item")
    inp1=input(" bill you want print press yes not press no:")
    if inp1=="yes":
        pass
        if finalamount!=0:
            print(25*"=","surendra supermarket",25*"=")
            print(25*"=","palnadhu")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ","item",8*" ","Quntity",3*" ","price")
            for i in range(len(pricelist)):
                print(i,8*" ",8*" ",ilist[i], 3*" ", qlist[i],8*' ', plist[i])
            print(75*"-")
            print(50*" ","totalamount:","RS",finalamount)
            print("gst amount",40*" ","gst",gst)
            print(75*"-")
            print(20*" ","thanks for visiting")
            print(75*"-")




            


        


