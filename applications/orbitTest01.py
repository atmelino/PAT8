import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from random import randint
import traceback
import os
from scipy.integrate import odeint
import math
import json
import sys

# https://en.wikipedia.org/wiki/Hohmann_transfer_orbit
#print 'Argument List:', str(sys.argv)
#print sys.argv[1:2]
#print sys.argv[1]
data=sys.argv[1:2]
decoded = json.loads(sys.argv[1])
#print decoded
#print decoded['x0']
central=decoded['central']
x0=decoded['x0']
y0=decoded['y0']
vx0=decoded['vx0']
vy0=decoded['vy0']
z0=0
GM=decoded['GM']
tf=decoded['tf']


#GM = 1.5

#print GM/2
#r = math.sqrt(x0 * x0 + y0 * y0 + z0 * z0)    
#rcubed = r * r * r
#print rcubed
#muorc = -1.0 * GM / rcubed
#print muorc




def acceleration(r_vec, t):
    x, y, z, vx, vy, vz = r_vec
    #mu = 3000.0
    r = math.sqrt(x * x + y * y + z * z)    
    rcubed = r * r * r
    #muorc = -1.0 * mu / rcubed
    muorc = -1.0 * GM / rcubed
    #print r
    drdt = [vx, vy, vz, muorc * x, muorc * y, muorc * z]
    return drdt

def npmax(l):
    max_idx = np.argmax(l)
    max_val = l[max_idx]
    #return (max_idx, max_val)
    return max_val

def npmin(l):
    min_idx = np.argmin(l)
    min_val = l[min_idx]
    #return (min_idx, min_val)
    return min_val

t = np.linspace(0, tf, 100)
y_vec0 = [x0, y0, 0, vx0, vy0, 0]
#y_vec0 = [0, 20, 0, 16, 0, 0]
print 'y_vec0 ',y_vec0,

sol = odeint(acceleration, y_vec0, t)


try:
    os.remove("writeFiles/orbitTest01.png")
except Exception: 
    pass

try:
    if central=='Earth':
        circle1=plt.Circle((0,0),6378,color='#36AFBF')
        #77 182 196
        plt.gcf().gca().add_artist(circle1)
    if central=='Sun':
        circle1=plt.Circle((0,0),6963000,color='#E9F073')
        plt.gcf().gca().add_artist(circle1)
    #plt.plot(range(5))
    # plt.plot(t, s)    
    plt.plot(sol[:, 0], sol[:, 1])
    #print npmax(sol[:, 0])
    #print npmax(sol[:, 1])
    #print npmin(sol[:, 1])
    ps1=npmax(sol[:, 0])
    ps2=np.absolute(npmin(sol[:, 0]))
    ps3=npmax(sol[:, 1])
    ps4=np.absolute(npmin(sol[:, 1]))
    print max(ps1,ps2,ps3,ps4)
    plotsize=1.01*max(ps1,ps2,ps3,ps4)
    
    plt.xlim(-plotsize, plotsize)
    plt.ylim(-plotsize, plotsize)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.draw()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('central body orbit')
    plt.grid(True)
    plt.savefig("writeFiles/orbitTest01.png", bbox_inches='tight')
except Exception:
    print(traceback.format_exc())
    print "exception"
    print "end"
