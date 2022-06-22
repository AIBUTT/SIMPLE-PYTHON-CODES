import sys
import math
from matplotlib import pyplot as plt
import numpy as np

x = float(sys.argv[1])
y = float(sys.argv[2])

R = math.hypot(x,y)
A = math.atan2(y,x)

print("RADIUS:% 3d, ANGLE:% 3d" %(R, math.degrees(A)))

X = [0.0, x]
Y = [0.0, y]

plt.plot(X,Y)
plt.show()

