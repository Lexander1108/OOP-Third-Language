import math
num = int(input("Enter x:"))
num2 = int(input("Enter y:"))
num3 = int(input("Enter z:"))
a = ( ( math.sqrt(abs(num-1) ))-pow(abs(num2),1/3) )/(1+( (num**2)/2) + ((num2**2)/4))
print ("a=", a)
b = num*(math.atan(num3))+pow(math.e,-(num+3))
print ("b=",b)
