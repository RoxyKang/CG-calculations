import numpy as np

a = np.array([0.5,-0.8,0.6])
b = np.array([0.6,3,-0.7])
c = np.array([-0.7,-0.5,-0.5])

n = np.array([0,-1,0])
n = n/np.linalg.norm(n)

p = np.array([0,1,0])

# !!! UPDATE a & b, depending which segment is intersected
d1 = np.dot(n, a-p)
d2 = np.dot(n, b-p)

t = d1/(d1-d2)

# !!! UPDATE a & b, depending which segment is intersected
I = a + t * (b-a)

print("The intersection point: ", I)