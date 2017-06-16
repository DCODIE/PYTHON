"""Write a python program to execute the following lines code by catching appropriate exception without runtime errors.
1)	print (1+’msrit’)
2)	L = [1,2,3]
print(L[4])"""
try:
  print(1+'msrit')
except TypeError:
  print ("That was not a valid concatenation.  Try again…")
L=[1,2,3]
try:
  print(L[4])
except IndexError:
  print("list index out of range")
