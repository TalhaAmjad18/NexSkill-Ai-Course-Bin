#Python Program to Find the Area of a Triangle[The program takes three sides of a triangle and 
# prints the area formed by all three sides.]

import math

a = int(input("Enter first side of triangle: "))

b = int(input("Enter second side of triangle: ")) 

c = int(input("Enter third side of triangle: "))

s = ( a + b + c ) / 2

area = math.sqrt( s * ( s - a ) * ( s - b ) * ( s - c ) )

print(f"Area of triangle: {area:.2f}")