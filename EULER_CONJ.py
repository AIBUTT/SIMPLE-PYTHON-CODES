import sys
import math

i,j,k,l = 3,4,5,6

for i in range(21,30):
    for j in range(81,90):
        for k in range(105,115):
            for l in range(130,135):
                for m in range(140,150):
                    x = i**5 + j**5 + k**5 + l**5 
                    if x == m**5:
                        print(i,j,k,l,m)
                        break

