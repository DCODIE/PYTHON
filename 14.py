"""Write a python function called is_abecedarian that returns True if :
the letters in a word appear in alphabetical order (double letters are ok) 
How many abecedarian words are there?"""
def is_abecderian(s):
    if s==''.join(sorted(s)):
        return True
    return False
a=input("enter the string")
lists=a.split()
c=0
for i in lists:
    if is_abecderian(i):
        c+=1
print("number of abecederian words are:",c)
