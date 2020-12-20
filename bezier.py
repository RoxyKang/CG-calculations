import numpy as np

# The three points of a curve
P0 = np.array([19,28,0])
P1 = np.array([-8,29,0])
P2 = np.array([19,-2.5,0])

R1 = ((P2-P0) / 6) + P1
L2 = (P1-R1) + P1
L1 = ((P0-P1) / 3) + L2
R2 = ((P2-P1) / 3) + R1

print("R1: ", R1, "L2: ", L2, "L1: ", L1, "R2: ", R2)