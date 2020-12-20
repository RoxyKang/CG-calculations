import numpy as np

a = np.array([0.1,-0.8,0])
b = np.array([1.7,0.2,0.9])
c = np.array([-0.8,0.6,0])

p = np.array([1, 0, 0])

n = np.array([-1,0,0])

pa = a - p
pb = b - p

d1 = np.dot(n, pa)
d2 = np.dot(n, pb)

t = d1/(d1-d2)

I = a + t*(b-a)

print(I)
