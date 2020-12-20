import numpy as np

pl = np.array([90, -60, 0])
pr = np.array([90, 30, 0])
p = np.array([90, -24.7766, 0])

pl_c = np.array([0, 255, 0])
pr_c = np.array([0,0,255])

c1 = np.linalg.norm(p - pl)
c2 = np.linalg.norm(pr - p) 

print(c1+c2)

print(np.linalg.norm(pl-pr))

p_c = c2/(c1+c2) * pl_c + c1/(c1+c2) * pr_c

print(p_c)
# print(p_c/np.linalg.norm(p_c))