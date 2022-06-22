import sys
import math

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

MIN = min(x,y)
MIN = min(MIN,z)

MAX = max(x,y)
MAX = max(MAX,z)

print("MAX:% 3d, MIN:% 3d" %(MAX, MIN))

