import numpy as np 

v0 = np.array([0.5801, -0.8146, 0])
v1 = np.array([0.9655, -0.2604, 0])

v0 = v0/np.linalg.norm(v0)
v1 = v1/np.linalg.norm(v1)

theta1 = np.arccos(np.dot(v0, v1))

print(np.rad2deg(theta1))