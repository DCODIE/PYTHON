#If Input: Robert B. Qwerty   then Output : RBQ
def initials():
    s=input("enter name")
    s=s.title()
    s=s.split()
    s3=[]
    for i in range (0,len(s)):
        s3.append(s[i][0])
    s3=''.join(s3)
    print(s3)
initials()
