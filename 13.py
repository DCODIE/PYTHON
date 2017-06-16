"""Write a python program to enter name, phone number and email-id separated by spaces in the following format and store it in list or file.
Alex  80-23345676   alex234@gmail.com
Emily 322-45676412 em_44@yahoo.com
Phone number contains 3 or 2 digit area code and a hyphen followed by 8 digit number. 
Perform the following using regular expressions
i)	Find all the phone numbers having 4 consecutive 0s at the end
ii)	Find all the total number of people having Gmail-ID 
iii)	Find all the names whose phones are not in proper format"""
import re
pat="\w+@gmail.com"
pat1="\d{2,3}-\d{8}\s"
ch=1
L=[]
while(ch==1):
    L.append(input("Enter details"))
    ch=int(input("Add new details?(1/0)"))
print("Numbers ending with 0000")
for i in L:
    L1=i.split()
    if re.search("0000$",L1[1]):
        print(L1[1])
print("People with gmail account")
for i in L:
    L1=i.split()
    if re.match(pat,L1[2]):
        print(L1[2])
print("People with phones not in proper format")
for i in L:
    L1=i.split()
    if re.match(pat1,L1[1]+" "):
        continue
    print(L1[0])
