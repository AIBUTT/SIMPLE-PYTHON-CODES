# CALCULATES QUADRATIC ROOTS OF AX^2 + BX + C = 0

import sys
import math

A = float(sys.argv[1])
B = float(sys.argv[2]) 
C = float(sys.argv[3])

D = B**2 - 4.0*A*C

if (D < 0.0):
    print("IMAGINARY ROOT")
else:
    E = math.sqrt(D)
    print("FIRST ROOT IS:", (-B + E)/(2.0*A))
    print("SECOND ROOT IS:", (-B - E)/(2.0*A))


