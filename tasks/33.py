from math import *
x = int(input("Enter x:"))
y = int(input("Enter y:"))
#print("max(x, y) is:", max(x, y))
#print("min (x, y) is:", min (x, y))
#print("max(x,y), min(x,y) is:", max(x,y), min(x,y))
if x > y:
    print("max is:", max(x,y))
    print("min is:", min(x,y))
elif x == y:
    print("x is equal y.")
else:
    print("min is:", min(x,y))
    print("max is:", max(x,y))
