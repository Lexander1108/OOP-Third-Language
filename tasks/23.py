import math
a = int(input("Enter first side:"))
b = int(input("Enter second side:"))
c = int(input("Enter third side:"))
p = 1/2*(a+b+c)
h_a = (2*math.sqrt(p*(p-a)*(p-b)*(p-c)))/a
print("a height is:", h_a)
h_b = (2*math.sqrt(p*(p-a)*(p-b)*(p-c)))/b
print("b height is:", h_b)
h_c = (2*math.sqrt(p*(p-a)*(p-b)*(p-c)))/c
print("c height is:", h_c)
m_a = 1/2*math.sqrt((2*a**2)+(2*b**2)-a**2)
print("a median is:", m_a)
m_b = 1/2*math.sqrt((2*a**2)+(2*b**2)-b**2)
print("b median is:", m_b)
m_c = 1/2*math.sqrt((2*a**2)+(2*b**2)-c**2)
print("c median is:", m_c)
l_a = (2*math.sqrt(a*b*p*(p-a)))/(b+c)
print("a bisector is:", l_a)
l_b = (2*math.sqrt(a*b*p*(p-b)))/(a+c)
print("b bisector is:", l_a)
l_c = (2*math.sqrt(a*b*p*(p-c)))/(b+a)
print("c bisector is:", l_a)
in_c = math.sqrt(((p-a)*(p-b)*(p-c))/p)
print("Inscribed circle radius is:", in_c)
cm_c = (a*b*c)/4*(math.sqrt(p*(p-a)*(p-b)*(p-c)))
print ("Circumscribed circle radius is:", cm_c)




