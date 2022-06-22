import sys
import math
import random

#   x = float(sys.argv[1])

L1 = ['C', 'D', 'H', 'S']   # CLUB, DIAMOND, HEART, SPAD
L2 = []
for i in range(0,13):
    L2.append(str(i+1))
L3 = L2[:]; L4 = L2[:]; L5 = L2[:]
for i in range(0,13):
        L2[i] = L1[0] + L2[i]
        L3[i] = L1[1] + L3[i]
        L4[i] = L1[2] + L4[i]
        L5[i] = L1[3] + L5[i]
L = L2 + L3 + L4 + L5
print(L)
random.shuffle(L)
print(L)
#random.shuffle(L)
#print(L)
