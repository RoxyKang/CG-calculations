import numpy as np

# Compute the refracted angle of a ray entering from one medium to another
# _in is the value for the ray BEFORE entering the medium
idx_in = 1.0
idx_out = 1.5

angle_in = np.deg2rad(75.749)

angle_out = np.arcsin(idx_in * np.sin(angle_in) / idx_out)

print("angle out in degree: ", np.rad2deg(angle_out), "in rad: ", angle_out)