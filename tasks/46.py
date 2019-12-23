import math
a = int(input('Enter first intrger: \t'))
b = int(input('Enter second intrger: \t'))
if a and b < 0:
    a = math.sqrt(a)
    b = math.sqrt(b)
    print(a, b)
elif a or b < 0:
    a += 0.5
    b += 0.5
    print(a, b)
elif (a and b > 0) and (a and b != (0.5<(a and b)<2.0)):
    (a and b)/10
    print('Both integers devided by 10 ', a, b)
else:
    print(a, b)

    