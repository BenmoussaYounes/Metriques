import numpy as np

def Euclidean_distance(p1, p2):
    dist = (p1[0]-p2[0])**2+(p1[1]-p2[1])**2
    euclidean_distance =  np.sqrt(dist)
    return euclidean_distance

# Consider the two point with 2 dimensions p1 and p2
p1 = [1,1]
p2 = [2,2]

# Calculating Euclidean Distance
print('Euclidean_distance  : ', Euclidean_distance(p1, p2))