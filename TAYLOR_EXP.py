import sys
import math

x = float(sys.argv[1])

R = 0.0
E = 10.0
i = 1.0
TERM = 1.0
while R != R + TERM:
    R = R + TERM
    TERM = TERM*x/i
    i += 1.0

print(R,i)

