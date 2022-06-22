import sys
import math

n = int(sys.argv[1])

H_S = 0.0
for i in range(1, n+1):
    H_S = H_S + 1.0/float(i)

print("THE HARNOMIC SUM OF % 1d TERMS IS % 1.5f" %(n,H_S))
print(n, H_S)

