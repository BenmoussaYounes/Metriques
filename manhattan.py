
import numpy as np



# Consider the two point with 2 dimensions p1 and p2

def Manhattan_distance(p1,p2):
 dist = 0
 for i in range(len(p1)):
     dist = dist + abs(p1[i] - p2[i])
 return dist

# Consider the two list a and b

A = [2, 4, 4, 6]
B = [5, 5, 7, 8]


# Calculating Euclidean Distance
print('Manhattan_distance  : ', Manhattan_distance())
