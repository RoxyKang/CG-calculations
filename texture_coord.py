import numpy as np

# World coord of the vertices of the triangle
a = np.array([])
b = np.array([])
c = np.array([])

# Texture coord of the same three points
a_text = np.array([])
b_text = np.array([])
c_text = np.array([])

# World coord of a point  --> we want to compute its color
p = np.array([])

# Calculate the barycentric coord of this point p
# a,b,c: vertices of the triangle
v_ab = b-a
v_ac = c-a

At = 1/2 * np.linalg.norm((np.cross(v_ab, v_ac)))

v_pa = a-p
v_pb = b-p
v_pc = c-p

Aa = 1/2 * np.linalg.norm(np.cross(v_pb, v_pc))
Ab = 1/2 * np.linalg.norm(np.cross(v_pa, v_pc))
Ac = 1/2 * np.linalg.norm(np.cross(v_pa, v_pb))

# Multiply the barycentric coord by the texture coord of abc --> end up with the text coord of p
p_text = Aa * a_text + Ab * b_text + Ac * c_text

# Then we know the corressponding color

