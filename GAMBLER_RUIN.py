import sys
import math
import random
import numpy as np

x1 = int(sys.argv[1])    #   X IS STAKES
y1 = int(sys.argv[2])    #   Y IS GOAL
z1 = int(sys.argv[3])    #   Z IS TOTAL TRIAL

TR = [] # TRIAL RESULTS
SIM = [] # TREND OF RISING OR FALLING STAKES IN ONE TRAIL
WIN = 0
for z in range(1,z1+1):
    x = x1
    y = y1 
    i=0
    while (x > 0 and x < y):
        if random.randrange(0,2) == 0:
            x += 1; SIM.append(x);
            i += 1
            if x == y:
                WIN += 1
        else:
            x -= 1; SIM.append(x);
            i += 1

    TR.append(i)

print("YOU WILL WIN % 1d TIMES PER % 1d EXPERIMENTS WITH A WIN PERCENTAGE OF % 3.1f" %(WIN, z1, WIN/z1*100.0))

print("ON AN AVERAGE, YOU WILL BET % 1d TIMES PER EXPERIMENT BEFORE YOU EITHER REACH YOUR GOAL OR RUN OUT OF STAKES" %(np.sum(TR)/z1))

#print(SIM)

