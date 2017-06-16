#calculate the area of the circle and catch appropriate user defined exception.
class NegativeRadius(Exception):
    def __init__(self):
        print("Radius is negative")
        quit()
def main():
    try:
        r=int(input("Enter the radius of the circle"))
        if r<0:
            raise NegativeRadius
        else:
            print("Area of circle is "+str(3.14*r*r))
    except ValueError:
        print("Not a number")
main()
