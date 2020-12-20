import numpy as np

# a,b,c: vertices of the triangle
a = np.array([0,4,0])
b = np.array([4,4,0])
c = np.array([3,0,0])

# p: a point 
p = np.array([3.5,2,0])

v_ab = b-a
v_ac = c-a

At = 1/2 * np.linalg.norm((np.cross(v_ab, v_ac)))

v_pa = a-p
v_pb = b-p
v_pc = c-p

Aa = 1/2 * np.linalg.norm(np.cross(v_pb, v_pc))
Ab = 1/2 * np.linalg.norm(np.cross(v_pa, v_pc))
Ac = 1/2 * np.linalg.norm(np.cross(v_pa, v_pb))

print("alpha: ", Aa/At, "beta: ", Ab/At, "gamma: ", Ac/At)
print("sum: ", Aa/At+Ab/At+Ac/At)

c1 = np.array([112,125,55])
c2 = np.array([255,125,0])
c3 = np.array([255,125,0])

color = c1 * (Aa/At) + c2 * (Ab/At) + c3 * (Ac/At)

print(color)
