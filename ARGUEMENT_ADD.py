#   THIS PROGRAM READS ARGUMENTS FROM USER WITHIN EXECUTION COMMAND
import sys

x = sys.argv[1]
y = sys.argv[2]

print("x + y = ",float(x) + float(y))

print("SHE HAS ", x, "APPLES AND ", y, "ORANGES.")

for i in range(5):
    print("COUNT", i, "TIMES")

a = 5
print(id(a))
a = a + 1
print(a)
print(id(a))

