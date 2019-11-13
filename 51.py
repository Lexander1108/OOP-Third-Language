import math
a = int(input('Enter a: \t'))
b = int(input('Enter b: \t'))
c = int(input('Enter c: \t'))
if a == 0:
    print('a shouldn`t be equal 0!')
else:
    d = b**2 - (4 * a * c)
    b * (-1)
    t1 = (b + (math.sqrt(d)))/2*a
    t2 = (b - (math.sqrt(d)))/2*a
    print('t1 = ', t1)
    print('t2 = ', t2)