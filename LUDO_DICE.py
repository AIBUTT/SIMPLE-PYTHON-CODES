import sys
import math
import random

print("LETS ROLL THE DICE")

while True:
    print("DO YOU WANT TO ROLL?")
    x=str(input())
    if (x=="y" or x=="Y" or x=="yes" or x=="YES" or x=="Yes"):
        print(random.randint(1,6), random.randint(1,6))
    elif (x=="n" or x=="no" or x=="N" or x=="No" or x=="NO"):
        print("HOW UNFORTUNATE THAT YOU DON'T WANT TO PLAY!!!")
        print("GOOD BYE")
        break

