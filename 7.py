"""Python list reverse method Input :   hello world cse 326 32.545 ostrich quit 
Output: ostrich 32.545 326 cse hello world"""
list = []
while True:
    line = input()
    if line:
        if line=="quit":
            break
        else:
            list.append(line)
newlines=list[::-1]
print('\n'.join(newlines))

