import math

x1 = [4.2, 3.6, 1.0]
x2 = [5.7, 2.8, -1.5]

euclideanDistance = 0
for i in range(len(x1)):
    euclideanDistance += (x1[i] - x2[i])**2

print (math.sqrt(euclideanDistance))