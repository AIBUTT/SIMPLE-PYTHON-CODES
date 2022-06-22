# LETS WITNESS ROUNDING OFF PROBLEM HERE

import sys
import math

print("THE ARGUMENT IS TAKEN IN DEGREE")

x = float(sys.argv[1])
x = math.radians(x)

print((math.sin(x))**2 + (math.cos(x))**2)

