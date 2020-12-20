import numpy as np

torusC = np.array([45.63,0,0]) # center of the torus
torusN = np.array([0,0,1]) # normal of the torus
torusR1 = 45.63 # R1 (center of the torus to the center of its tube)
torusR2 = 16.96 # R2 (radius of its tube)
rayO = np.array([-72,0,-27])
rayD = np.array([-1,-1,-1])

rayD = rayD/np.linalg.norm(rayD)
torusN = torusN/np.linalg.norm(torusN)

k = (rayO - torusC) * torusN
p = rayO - (torusN * k) # The projection point of rayO on the plane of the torus

M = (p - torusC) / np.linalg.norm(p-torusC)
m = M * torusR1 + torusC

D = np.linalg.norm(m-rayO) - torusR2
print("Point p, the projection of rayO to xy-plane, is: ", p)
print("Point m, P's closest point to torus medial axis, is: ", m)
print("The smallest distance from the camera to the torus is: ", D)