a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
p = (a+b+c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Answer is:", s)