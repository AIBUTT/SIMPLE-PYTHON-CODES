import sys
import math
import random

x = int(sys.argv[1])
y = int(sys.argv[2])

# TWO FAIR DICE AND THEIR SUM

for i in range(10):
    R1 = random.randint(x,y)
    R2 = random.randint(x,y)
    print("DICE A: % 1d, DICE B: % 1d, SUM: % 2d" %(R1, R2, R1+R2))

