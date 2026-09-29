import numpy as np

class VectorDistance:
    def euclidean(self, a, b):
        #distance = np.linalg.norm(a - b)
        distance = np.sqrt(np.sum((a - b) ** 2))
        return distance

    def manhattan(self, a, b):
        distance = np.sum(np.abs(a - b))
        return distance

    def minkowski(self, a, b, p):
        p = 3
        distance = np.sum(np.abs(a - b) ** p) ** (1/p)
        return distance

    def chebyshev(self, a, b):
        distance = np.max(np.abs(a - b))
        return distance


a=np.array([1,2,3])
b=np.array([3,2,5])

vDistance=VectorDistance()
Edist=vDistance.euclidean(a,b)
print(Edist)