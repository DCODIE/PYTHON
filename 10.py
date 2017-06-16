"""Read the marks for three subjects from the command line. 
If the CIE marks is less than 20, the exception ‘MarksNotElligible’ is  thrown . 
If the given marks is not a valid integer  then exception must be handled"""
import sys
class MarksNotEligible(Exception):
    def __init__(self):
        print("fail")
        quit()
for i in range(len(sys.argv)):
        if(i==0):
            continue
        else:
            try:
                n = int(sys.argv[i])
                print(n)
            except ValueError:
                print("invalid int")
                quit()
            else:
                if(int(sys.argv[i])<20):
                    raise MarksNotEligible
print("pass")
