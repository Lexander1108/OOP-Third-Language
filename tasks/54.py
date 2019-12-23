x1 = int(input('Enter x1: \t'))
x2 = int(input('Enter x2: \t'))
x3 = int(input('Enter x3: \t'))
y1 = int(input('Enter y1: \t'))
y2 = int(input('Enter y2: \t'))
y3 = int(input('Enter y3: \t'))
def check (x1, y1, x2, y2, x3, y3):
    ((x2 - x1) * (y3 - y1) * (x3 - x1) * (y2 - y1))/2
# if check(x1, y1, x2, y2, x3, y3) == 
#     check(0, 0, x2, y2, x3, y3) ==
#     check(x1, y1, 0, 0, x3, y3) == 
#     check(x1, y1, x2, y2, 0, 0):
#     print('Belongs')
# else:
#     print('Doesn`t belong')
