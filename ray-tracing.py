import numpy as np

S = np.array([0,0,0]) # The center of the sphere
r = 35 # The radius of the sphere
C = np.array([-74,-20,-12]) # The position of the camera 
ray = np.array([1,0,0]) # Ray


########################
norm_ray = np.linalg.norm(ray)
normal_ray = ray/norm_ray

V1 = S - C
norm_V1 = np.linalg.norm(V1)
normal_V1 = V1/norm_V1

theta = np.arccos(np.dot(normal_ray, normal_V1))

D1 = np.dot(V1, normal_ray)
d = D1 * np.tan(theta)
a = np.sqrt(r**2 - d**2)
b = D1 - a
I = (normal_ray*b) + C

n = I - S
sphere_n_norm = np.linalg.norm(n)
sphere_normal = n/sphere_n_norm

print("Intersection: ", I, "Normal of the intersection: ", sphere_normal)