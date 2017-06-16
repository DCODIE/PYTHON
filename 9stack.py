s=[]
def Getstack():
    s=[]
    return s
def isEmpty():
    if len(s)==0:
        return True
    else:
        return False
def Top():
    return len(s)-1
def Push(item):
    s.append(item)
def Pop():
    return s.pop()
