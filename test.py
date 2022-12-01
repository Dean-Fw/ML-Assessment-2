import math

x1 = [4.2, 3.6, 1.0]
x2 = [5.7, 2.8, -1.5]

x1Sum = None
x2Sum = None

for i in range(len(x1)):
    if not x1Sum:
        x1Sum = x1[i]
    else:
        x1Sum -= x1[i]

x1Sum = x1Sum ** 2

for i in range(len(x2)):
    if not x2Sum:
        x2Sum = x2[i]
    else:
        x2Sum -= x2[i]

x2Sum = x2Sum ** 2

total = x1Sum + x2Sum
total = math.sqrt(total)
euclideanDistance = total

print (euclideanDistance)