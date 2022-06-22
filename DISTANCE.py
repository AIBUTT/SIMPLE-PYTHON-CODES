# CALCULATE CARTESIAN DISTANCE FROM ORIGIN

import sys
import math

print("HELLO CLASS")
#x = float(sys.argv[1]) 
#y = float(sys.argv[2])

x = input()
print("You have entered a value for x")
y = input()
print("You have entered a value for y")


d1 = math.sqrt(x**2 + y**2)

d2 = math.hypot(x,y)

print(d1, "AND", d2)

