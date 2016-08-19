from scipy.optimize import rosen, rosen_der, rosen_hess
import scipy.optimize as opt
import numpy as np
import matplotlib.pyplot as plt

global ps


def reporter(p):
    """Reporter function to capture intermediate states of optimization."""
    global ps
    ps.append(p)



# Initial starting position
x0 = np.array([4,-4.1])
ps = [x0]

opt.minimize(rosen, x0, method='Newton-CG', jac=rosen_der, hess=rosen_hess, callback=reporter)

ps = np.array(ps)

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = rosen(np.vstack([X.ravel(), Y.ravel()])).reshape((100,100))

plt.figure(figsize=(12,4))
plt.subplot(121)
plt.contour(X, Y, Z, np.arange(10)**5)
plt.plot(ps[:, 0], ps[:, 1], '-o')
plt.subplot(122)
plt.semilogy(range(len(ps)), rosen(ps.T));

