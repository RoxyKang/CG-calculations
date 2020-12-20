import numpy as np
from scipy.spatial.transform import Rotation as R

ray = np.array([0.984808, 0.173648, 0]) # TODO
ray = ray / np.linalg.norm(ray)
N1 = 1.33
N2 = 2.42

# step 1, calculate the in-intersection point
in_intersection = np.array([-8.8073, 31.1927, 0]) # TODO

# step 2, use bilinear to calculate the interpolated normal
pl = np.array([-40, 0, 0])
pr = np.array([0, 40, 0])
p = in_intersection

pl_c = np.array([np.cos(np.deg2rad(135)), np.sin(np.deg2rad(135)), 0])
pr_c = np.array([0,1,0])

c1 = np.linalg.norm(p - pl)
c2 = np.linalg.norm(pr - p) 
p_c = c2/(c1+c2) * pl_c + c1/(c1+c2) * pr_c
p_c = p_c / np.linalg.norm(p_c)

print("Interpolated normal of in-intersection point: " ,p_c)

# step 3, calculate the angle of the interpolated normal and the original ray
v0 = -ray
v1 = p_c

theta1 = np.arccos(np.dot(v0, v1))

print("Angle between the in-intersection interpolated normal and the original ray: ", np.rad2deg(theta1))

# step 4, use snells rule to calculate the refraction angle
theta2 = np.arcsin(N1*np.sin(theta1)/N2)

print("refraction angle, in: ", np.rad2deg(theta2))

# step 5, use rotation matrix to calculate the rotated ray direction
rotation_axis = np.array([0,0,1])
rotation_vector = -(theta1-theta2) * rotation_axis
rotation = R.from_rotvec(rotation_vector)
rotated_vec = rotation.apply(ray)
rotated_vec_normal = rotated_vec/np.linalg.norm(rotated_vec)

print("refracted ray, in: ", rotated_vec_normal)

# # step 6, calculate the out-intersection point
out_intersection = np.array([29.6461, -10.3539, 0]) # TODO

# step 7, use bilinear to calculate the interpolated normal
# TODO
pl = np.array([40, 0, 0])
pr = np.array([0, -40, 0])
p = out_intersection

pl_c = np.array([np.cos(np.deg2rad(315)), np.sin(np.deg2rad(315)), 0])
pr_c = np.array([0,-1,0])

c1 = np.linalg.norm(p - pl)
c2 = np.linalg.norm(pr - p) 
p_c = c2/(c1+c2) * pl_c + c1/(c1+c2) * pr_c
p_c = p_c / np.linalg.norm(p_c)

print("Interpolated normal of out-intersection point: " ,p_c)

# step 8, calculate the angle between the interpolated normal and the rotated ray
v0 = rotated_vec_normal
v1 = p_c

theta1 = np.arccos(np.dot(v0, v1))

print("Angle between the out-intersection interpolated normal and the rotated ray: ", np.rad2deg(theta1))

# step 9, use rotation matrix to calculate the rotated out ray

N1 = 2.42
N2 = 1.33

theta2 = np.arcsin(N1*np.sin(theta1)/N2)

rotation_axis = np.array([0,0,1])
rotation_vector = -(theta1-theta2) * rotation_axis
rotation = R.from_rotvec(rotation_vector)
rotated_vec = rotation.apply(rotated_vec_normal)
rotated_vec_normal = rotated_vec/np.linalg.norm(rotated_vec)

print("refracted ray, out: ", rotated_vec_normal)

# step 10, calculate the angle between the interpolated normal and the refracted out ray
v0 = rotated_vec_normal
v1 = p_c

theta1 = np.arccos(np.dot(v0, v1))

print("Angle between the out-intersection interpolated normal and the out ray: ", np.rad2deg(theta1))

# step 11, calculate the intersection point of the out ray with the color plane
P = np.array([90,-70,0]) # TODO
C = out_intersection
ray = rotated_vec_normal
n = np.array([-1,0,0])

########################
W = P - C
a = np.dot(W, n)
b = np.dot(ray, n)
k = a/b
I = (ray * k) + C

print("Intersection on the color plane: ", I)

# step 12, use bilinear to calculate the interpolated color
pl = np.array([90, -70, 0])
pr = np.array([90, 30, 0])
p = I

pl_c = np.array([0, 255, 0])
pr_c = np.array([0,0,255])

c1 = np.linalg.norm(p - pl)
c2 = np.linalg.norm(pr - p) 

p_c = c2/(c1+c2) * pl_c + c1/(c1+c2) * pr_c

print("Interpolated color: ", p_c)