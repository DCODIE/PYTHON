def vow(str):
    #s="abcd"
    vc=0
    for i in range(len(str)):
        if str[i]=='a' or str[i]=='e' or str[i]=='i'  or  str[i]=='o' or str[i]=='u':
            vc+=1
        else:
            continue
    print(vc)
