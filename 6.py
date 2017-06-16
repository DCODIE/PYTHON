#number of occurrences of each vowels in the string
def vow(str):
    ac=ec=ic=oc=uc=0
    for i in range(len(str)):
        if str[i]=='a':
            ac +=1
        elif str[i]=='e':
            ec+=1
        elif str[i]=='i':
            ic+=1
        elif str[i]=='o':
            oc+=1
        elif str[i]=='u':
            uc+=1
        else:
            continue
    print('a e i o u')
    print(ac,ec,ic,oc,uc)
s=input()
vow(s.lower())
print(s)
