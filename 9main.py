#implement stack
from Sample import *
print("Initially stack is empty")
print(stack.Getstack())
while(1):
    print("1.Push")
    print("2.Pop")
    print("3.Top")
    ch=int(input("Enter your choice"))
    if ch==1:
        item=int(input("Enter item to push into stack"))
        stack.Push(item)
    elif ch==2:
        if(stack.isEmpty()):
            print("Stack is Empty")
        else:
            print(stack.Pop())
    elif ch==3:
        print(stack.Top())
    else:
        quit()
