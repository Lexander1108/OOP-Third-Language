from math import*
h = int(input('Enter h: \t'))
if h < 0:
    print('Equation doesn`t exist!')
else:
    nmt1 = abs(sin(8 * h)) + 17
    dnmt1 = (1 - sin(4 * h) * cos(h**2 + 18))**2
    a = sqrt(nmt1 / dnmt1)
    print('a is: ', a)
    dnmt2 = 3 + abs(tan(a * h**2) - sin(a * h))
    b = sqrt(3 / dnmt2)
    print('b is: ', b)
    c = a * h**2 * sin(b * h**3) * cos(a * h)
    print('c is: ', c)