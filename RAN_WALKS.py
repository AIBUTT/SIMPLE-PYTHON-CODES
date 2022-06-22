import sys
import math
import random

n = int(sys.argv[1])    # IF n IS ODD, BETTER
E = int(sys.argv[2])

T = []

for i in range(n):
    ROW = [False] * n
    T = T + [ROW]
    
FAIL = 0
for e in range(E):
    i = n//2
    j = n//2
    while (i>0) and (i<n-1) and (j>0) and (j<n-1):
        T[i][j] = True
        if (T[i+1][j]==True and T[i-1][j]==True and T[i][j+1]==True and T[i][j-1]==True):
            FAIL += 1
            for k in range(n):
                for l in range(n):
                    T[k][l]=False
            break

        r = random.randrange(1,5)
        if   ( r == 1 and T[i+1][j] == False ): i += 1 
        elif ( r == 2 and T[i-1][j] == False ): i -= 1
        elif ( r == 3 and T[i][j+1] == False ): j += 1
        elif ( r == 4 and T[i][j-1] == False ): j -= 1

#for ROWS in T: 
#    print(ROWS)

print(FAIL)

