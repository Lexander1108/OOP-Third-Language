x = int(input("Enter x:"))
y = int(input("Enter y:"))
first = 3*x*x*y*y
second = 2*x*y*y
third = 7*x*x*y
fourth = 4*y*y
fifth = 15*x*y
sixth = 2*x*x
seventh = 3*x
eighth = 10*y
r = first - second - third - fourth + fifth + sixth - seventh + eighth + 6
print("Answer is:", r)