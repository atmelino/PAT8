import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# x''(t)   + x(t)) = 0
# convert second order ode to first order system
# y'(t) = x(t)
# dydt(t) = -y'(t)

def func(y_vec, t):
    y, ydot = y_vec
    dydt = [ydot, -y]
    return dydt


y0 = [1, 0.0]

t = np.linspace(0, 10, 101)

sol = odeint(func, y0, t)

plt.plot(t, sol[:, 0], 'b', label='x(t)')
plt.plot(t, sol[:, 1], 'g', label='x_prime(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()

