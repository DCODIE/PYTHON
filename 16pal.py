def pal(str=input()):
    str2=str[::-1]
    if(str==str2):
        print("palindrome")
    else:
        print("not a palindrome")
pal()
