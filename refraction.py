import numpy as np
from scipy.spatial.transform import Rotation as R

C = np.array([-70,27,0])
ray = np.array([1,0,0])

# could use ray-plane to find the intersection point
n = np.array([-0.246171,0.969226,0]) # interpolated normal at the in-intersection

N1 = 1
N2 = 1.5

ray_normal = ray/np.linalg.norm(ray)
n_normal = n/np.linalg.norm(n)

# theta1 = np.arccos(np.dot(-ray_normal, n_normal)) # Defined by the angle between the normal and the ray
theta1 = np.deg2rad(75.749)
theta2 = np.arcsin(N1*np.sin(theta1)/N2)

print("refraction angle, in: ", np.rad2deg(theta2))

rotation_axis = np.array([0,0,1])
rotation_vector = -(theta1-theta2) * rotation_axis
rotation = R.from_rotvec(rotation_vector)
rotated_vec = rotation.apply(ray_normal)
rotated_vec_normal = rotated_vec/np.linalg.norm(rotated_vec)

print("refracted ray, in: ", rotated_vec_normal)

# Interpolated using bilinear, intersection point using Dylan
n = np.array([0.5801, -0.8146, 0]) # interpolated normal at the out-intersection

N1 = 1.5
N2 = 1

n_normal = n/np.linalg.norm(n)

theta1 = np.arccos(np.dot(rotated_vec_normal, n_normal))
theta2 = np.arcsin(N1*np.sin(theta1)/N2)

rotation_axis = np.array([0,0,1])
rotation_vector = -(theta1-theta2) * rotation_axis
rotation = R.from_rotvec(rotation_vector)
rotated_vec = rotation.apply(rotated_vec_normal)
rotated_vec_normal = rotated_vec/np.linalg.norm(rotated_vec)

print("refracted ray, out: ", rotated_vec_normal)
