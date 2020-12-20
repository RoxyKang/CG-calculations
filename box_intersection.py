import numpy as np

# Determine if the ray is intersecting with a box (defined by min and max)
# min: lower left corner; max: upper right corner

# Ray
rayO = np.array([-5.6,-7.1])
rayD = np.array([0.842403,0.538849])
rayD = rayD/np.linalg.norm(rayD)

# Define the grid in the question
grid_min = np.array([0,0])
grid_max = np.array([20,20])

Rprime = rayO + rayD * 1000 # far away from the plane 

# lower intersection wrt to y coord
a = np.abs(grid_min[1] - rayO[1])

k = a / np.abs(Rprime[1] - rayO[1])

Iy0 = (Rprime - rayO) * k + rayO

# upper intersection wrt to y coord
a = np.abs(grid_max[1] - rayO[1])

k = a / np.abs(Rprime[1] - rayO[1])

Iy1 = (Rprime - rayO) * k + rayO

# lower intersection wrt to x coord
a = np.abs(grid_min[0] - rayO[0])

k = a / np.abs(Rprime[0] - rayO[0])

Ix0 = (Rprime - rayO) * k + rayO

# upper intersection wrt to x coord
a = np.abs(grid_max[0] - rayO[0])

k = a / np.abs(Rprime[0] - rayO[0])

Ix1 = (Rprime - rayO) * k + rayO

print("Interval wrt to y coord: ", [Iy0, Iy1])
print("Interval wrt to x coord: ", [Ix0, Ix1])


