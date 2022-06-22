import sys
import math
import random

n = int(sys.argv[1])

W1 = 0
W2 = 0
for i in range(n):
    for j in range(0,6):
        if random.randint(1,6) == 6:
            W1 += 1
            break
    TWO = 0
    for k in range(0,12):
        if random.randint(1,6) == 6:
            TWO += 1
            if TWO == 2:
                W2 += 1
                break

print("""PROBABILITY OF GETTING 1 AT LEAST ONCE WHEN ROLLING A FAIR DIE SIX TIMES = {}
PROBABILITY OF GETTING 1 AT LEAST TWICE WHEN ROLLING A FAIR DIE 12 TIMES = {}""".format(W1/n, W2/n))
print(W1, W2, n)

