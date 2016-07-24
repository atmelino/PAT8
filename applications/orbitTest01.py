# import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from random import randint
import traceback
import os
from scipy.integrate import odeint



GM = 1.0

def acceleration(r, t):
    x, xdot, y, ydot = r
    dsq = dx * dx + dy * dy  # distance squared
    dr = math.sqrt(dsq)  # distance
    force = GM if dsq > 1e-10 else 0.
    xdotdot = force * x / dr
    ydotdot = force * y / dr
    drdt = [xdot, xdotdot, ydot, ydotdot]
    return drdt







t = np.linspace(0, 10, 101)
y0 = [0, 10, 20, 0]
#sol = odeint(acceleration, y0, t)


f = randint(0, 9)

t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2 * f * np.pi * t)


# print 7



try:
    os.remove("writeFiles/orbitTest01.png")
except Exception: 
    pass


try:
    plt.plot(t, s)    
    print 8
    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('Sine')
    plt.grid(True)



    # plt.savefig("test.png")
    # plt.show()
    plt.savefig("writeFiles/orbitTest01.png", bbox_inches='tight')
except Exception:
    print(traceback.format_exc())
    print "exception"
    print "end"


# matplotlib.style.use('ggplot')
