import math
hyp = int(input("Enter hyputenuse:"))
cath1 = int(input("Enter cathet:"))
cath2 = math.sqrt((hyp**2)-(cath1**2))
print ("Second cathet is:",cath2)
p = hyp+cath1+cath2
r = math.sqrt(((p-hyp)*(p-cath1)*(p-cath2))/p)
print ("Radius is:",r)
