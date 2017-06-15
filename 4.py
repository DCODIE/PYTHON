"""
(b)	Write a python program to design a class Account that stores the current balance, interest rate and account number of a bank account.
Your class should provide methods to withdraw deposit and add interest to the account. 
The user should only be allowed to withdraw money up to some overdraft limit. If an account goes overdrawn, there is fee charged. 
"""
class Account:
    od_limit=1000    #You can withdraw upto Rs.1000 extra other than balance
    od=0
    rate_of_int=0.07
    def __init__(self):
        self.balance=50          #initial balance
    def deposit(self,amt,acc_no):
        self.amt=amt
        self.acc_no=acc_no
        self.balance+=self.amt
        print("Your account number is %d"%(acc_no))
        print("Your current balance is %3f"%(self.balance))
    def wdraw(self,w):
        self.w=w
        self.balance=self.balance-self.w
        if self.balance<0:                      #if you withdraw more than you have
            self.od=abs(self.balance)
            print(self.od)#calc the extra amount withdrawn
            if self.od>Account.od_limit:        #check if it is more than od_limit
                if self.od<50:
                    self.fee=0.01*self.od

                elif self.od>50 and self.od<100:
                    self.fee=0.05*self.od
                else:
                    self.fee=0.07*self.od
                print("Fee charged is %3f"%(self.fee))

            else:
                print("Overdrawn money is %3f"%(self.od))
        else:
            print("Your balance after withdrawal is %3f"%(self.balance))
            self.rate()
    def rate(self):
        self.balance+=Account.rate_of_int*self.balance
        print("After interest by bank, your balance is %3f"%(self.balance))
person=Account()
amount=int(input("Enter the deposit amount :"))
acc=int(input("Enter account number :"))
person.deposit(amount,acc)
wd=int(input("Enter the amount to be withdrawn :"))
person.wdraw(wd)
