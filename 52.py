a = int(input('Enter a: \t'))
b = int(input('Enter b: \t'))
c = int(input('Enter c: \t'))
d = int(input('Enter d: \t'))
s = int(input('Enter s: \t'))
t = int(input('Enter t: \t'))
u = int(input('Enter u: \t'))
if s and t == 0:
    print('s and t shouldn`t be equal 0!')
else:
    if ( s* a + t * b + u) * (s * c + t * d + u) > 0:
        print('In one half-plane')
    else:
        print('In different half-planes')
    
