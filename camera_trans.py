import numpy as np

cameraPos = np.array([-50,-35,20])
targetPos = np.array([5,2,10])
upVec = np.array([0,0,1])

upVec = upVec / np.linalg.norm(upVec)

w = (cameraPos - targetPos) / np.linalg.norm(cameraPos - targetPos)

u = np.cross(upVec, w)
v = np.cross(w, u)

print("w: ", w, "u: ", u, "v: ", v)