import sys
import math

C = ['USA', 'ITALY', 'CHINA', 'SPAIN', 'GERMANY', 'FRANCE', 'UK']
TC = [116448.0, 92472.0, 81394.0, 72248.0, 56202.0, 37575.0, 17089.0]
D = [1943.0, 10023.0, 3295.0, 5812.0, 403.0, 2314.0, 1019.0]

PC = []

for i in range(7):
    PC.append(D[i]*100.0/TC[i])
    print("%10s: %-5.2f Per Cent" %(C[i], PC[i]))


