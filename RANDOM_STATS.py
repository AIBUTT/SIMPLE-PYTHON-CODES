import sys
import math
import random

n = int(sys.argv[1])

V = []

for i in range(n):
    V.append(random.random())

#print(round(V,3))
MIN_V = min(V)
MAX_V = max(V)
AVR_V = sum(V)/len(V)
print("MINIMUM VALUE: %6.2f, MAXIMUM VALUE: %6.2f, AVERAGE VALUE: %6.2f" %(MIN_V, MAX_V, AVR_V))

