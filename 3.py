"""(a)	Create a python dictionary for phones and their prices. Write functions to
a.	Add a new entry (phone:price) 
b.	Search for a particular phone and retrieve it’s price 
c.	Find phones with same price 
d.	Remove an entry.
e.	Display all phones sorted according to price. [Program must be menu driven]
"""
dict={}
def add():
    m=input("Enter name of the phone")
    p=float(input("Enter price of the phone"))
    d={m:p}
    dict.update(d)
def search():
    m=input("Enter name of the phone")
    if m not in dict:
        print("Particular Phone not found")
    else:
        print("Price of "+m+" is "+str(dict.get(m)))
def find():
    p=float(input("Enter the price"))
    for m,n in dict.items():
        if n==p:
            print(m)
def remove():
    m=input("Enter phone to remove")
    if m not in dict:
        print("Phone not found")
    else:
        del dict[m]
        print("Phone removed ")
def display():
    for key in sorted(dict,key=dict.get):
        print(key,dict[key])
def main():
    while(1):
        print("1.Add an entry")
        print("2.Search for a particular phone and retreive its price")
        print("3.Find phones with same price")
        print("4.Remove an entry")
        print("5.Display all phones according to sorted price")
        print("6.Quit")
        ch=int(input("Enter your choice"))
        if ch==1:
            add()
        elif ch==2:
            search()
        elif ch==3:
            find()
        elif ch==4:
            remove()
        elif ch==5:
            display()
        else:
            quit()
main()
