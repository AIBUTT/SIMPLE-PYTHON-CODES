import sys
import math

n = int(sys.argv[1])

P = []

for i in range(n+1):
    P.append(True)

for i in range(2, n):
    if P[i] == True:
        for j in range(2, n//i +1):
            #   print(i*j)
            P[i*j] = False

PN = []
for i in range(2,n):
    if P[i] == True:
        PN.append(i)

print(len(PN))
print(PN)

