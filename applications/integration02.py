#import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from random import randint
import traceback
import os
from scipy.integrate import odeint



f=randint(1,9)

# x''(t)   + x(t)) = 0
# convert second order ode to first order system
# y'(t) = x(t)
# dydt(t) = -y'(t)


def func(y_vec, t):
    y, ydot = y_vec
    dydt = [ydot, -f*y]
    return dydt


try:
    os.remove("writeFiles/integration02.png")
except Exception: 
    pass

try:
    y0 = [1, 0.0]
    t = np.linspace(0, 10, 101)
    sol = odeint(func, y0, t)
    
    plt.plot(t, sol[:, 0], 'b', label='x(t)')
    plt.plot(t, sol[:, 1], 'g', label='x_prime(t)')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid(True)
    plt.savefig("writeFiles/integration02.png", bbox_inches='tight')

except Exception:
    print(traceback.format_exc())
    print "exception"
    print "end"
