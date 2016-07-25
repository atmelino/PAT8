import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from random import randint
import traceback
import os
from scipy.integrate import odeint
import math

GM = 1.5

def acceleration(r_vec, t):
    x, y, z, vx, vy, vz = r_vec
    mu = 3000.0
    r = math.sqrt(x * x + y * y + z * z)    
    rcubed = r * r * r
    muorc = -1.0 * mu / rcubed
    #print r
    drdt = [vx, vy, vz, muorc * x, muorc * y, muorc * z]
    return drdt

t = np.linspace(0, 60, 100)
y0 = [0, 20, 0, 16, 0, 0]
print y0,

sol = odeint(acceleration, y0, t)


try:
    os.remove("writeFiles/orbitTest01.png")
except Exception: 
    pass

try:
    # plt.plot(t, s)    
    plt.plot(sol[:, 0], sol[:, 1])    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('orbit')
    plt.grid(True)
    plt.savefig("writeFiles/orbitTest01.png", bbox_inches='tight')
except Exception:
    print(traceback.format_exc())
    print "exception"
    print "end"
