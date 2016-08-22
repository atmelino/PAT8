import matplotlib.pyplot as plt
import numpy as np

# soa =np.array( [ [0,0,1,1,-2,0], [0,0,2,1,1,0],[0,0,3,2,1,0],[0,0,4,0.5,0.7,0]]) 
soa = np.array([ [-10000, 0, 0, 1000, 0, 0], [-5100   , 8577 , 0 , 513 , -863 , 0], [0, 0, 3, 2, 1, 0], [487, 9943 , 0 , -49 , -1008, 0]]) 
X, Y, Z, U, V, W = zip(*soa)

print U

# 1
plt.figure()
Q = plt.quiver(X, Y, U, V)
l, r, b, t = plt.axis()
dx, dy = r - l, t - b
factor = 0.5
plt.axis([l - factor * dx, r + factor * dx, b - factor * dy, t + factor * dy])
plt.show()
