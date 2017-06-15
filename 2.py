import re
def censor(file_name):
    f1=open(file_name,"r")
    f2=open("writing.txt","w")
    str=f1.read()
    s=re.sub(r'\b\w{4}\b','xxxx',str)

    f2.write(s)
    f1.close()
    f2.close()
def main():
    f1=open("sample.txt","w")
    f1.write("Welcome to Python.This is a programming lang\n")
    f1.write("This replaces four letter word\n")
    f1.close()
    censor("sample.txt")
main()
