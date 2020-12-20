import numpy as np

P = np.array([90,-60,0]) # A random point on the plane
C = np.array([31.1071, -8.8929, 0]) # The position of the camera
ray = np.array([0.9655, -0.2604, 0]) # Ray
n = np.array([-1,0,0]) # The normal of the plane

########################
norm_n = np.linalg.norm(n)
normal_n = n/norm_n

norm_ray = np.linalg.norm(ray)
normal_ray = ray/norm_ray

W = P - C
a = np.dot(W, normal_n)
b = np.dot(normal_ray, normal_n)
k = a/b
I = (normal_ray * k) + C

print("Intersection: ", I)