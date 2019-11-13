import math
R = float(input("Enter external ring radius:"))
r = 20
if R > 20:
    S = math.pi*((R**2)-(r**2))
    print ("Circle square is:", S )
else:
    print ("Enter correct value!")
    
    


