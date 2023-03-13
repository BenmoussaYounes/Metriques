import numpy as np

def Chebychef(vec1,vec2):
    dist= np.max(np.absolute(np.array(vec1) - np.array(vec2)))
    return dist