import math
a = int(input("Enter a:"))
b = int(input("Enter b:"))
if a < b:
    print("Error, a must be bigger than b!")
else:
    c = int(input("Enter board sides:"))
    alpha = int(input("Enter alpha:"))
    s1 = (a+b)/2
    s2 = math.sqrt(c**2-((a-b)**2)/4)
    s = s1*s2
    print("Answer is:", s)