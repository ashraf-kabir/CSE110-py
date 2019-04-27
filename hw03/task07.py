import math

x = float(input('Enter the value of first side of triangle\n'))
y = float(input('Enter the value of second side of triangle\n'))
z = float(input('Enter the value of third side of triangle\n'))

s = ((x+y+z)/2)

area = math.sqrt(s*(s-x)*(s-y)*(s-z))

print('Area of the triangle is '+str(area))
