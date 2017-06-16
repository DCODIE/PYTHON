#Implement Queue with INSERT,DELETE and DISPLAY operations
class MyQueue:
    MAX=7
    def __init__(self):
        self.q=[]
    def insert(self,ele):
        self.ele=ele
        self.q.append(self.ele)
        assert (len(self.q)<MyQueue.MAX),"The queue is full!"
    def remove(self):
        assert self.q!=[],"Empty queue!"
        self.r=self.q.pop(0)
        print("%d removed "%(self.r))
    def display(self):
        print(self.q)
q1=MyQueue()
print("1.insert 2.remove 3.display 4.quit")
while True:
    ch=int(input("Enter choice :"))
    if ch==1:
        n=int(input("Enter num :"))
        q1.insert(n)
    elif ch==2:
        q1.remove()
    elif ch==3:
        q1.display()
    else:
        break
