import math
a = int(input('Enter a integer: \t'))
b = int(input('Enter b integer: \t'))
c = int(input('Enter c integer: \t'))
# print(a, 'x2 + ', b, 'x + ', c, ' = 0')
if a == 0:
    print('a integer shouldn`t be equal 0!')
else:
    d = b**2 - (4*a*c)
    if d > 0:
        b*(-1)
        x1 = b + math.sqrt(d)/2*a
        x2 = b - math.sqrt(d)/2*a
        print('x1 is ', x1, 'x2 is ', x2)
    else:
        print('Equation doesn`t exist!')
