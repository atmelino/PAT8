import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import mpld3
from random import randint
import traceback
import os
from scipy.integrate import odeint
import math
import json
import sys
import matplotlib.path as mpath
import matplotlib.patches as mpatches

m_period = 27.321661547 * 86400
m_omega = 2 * np.pi / m_period
pos2D = np.empty((0, 2))
accel2D = np.empty((0, 2))
pos3D = np.empty((0, 3))
accel3D = np.empty((0, 3))

data = sys.argv[1:2]
decoded = json.loads(sys.argv[1])
central = decoded['central']
x0 = decoded['x0']
y0 = decoded['y0']
vx0 = decoded['vx0']
vy0 = decoded['vy0']
z0 = 0
GMearth = decoded['GMearth']
GMmoon = decoded['GMmoon']
t0 = decoded['t0']
deltat = decoded['deltat']
plotsize = decoded['plotsize']
global ax

def moonPosition(t):    
    mx = 300000 * np.sin(m_omega * t)
    my = 300000 * np.cos(m_omega * t)
    mz = 0
    mr = [mx, my, mz]
    return mr    
    
def acceleration(r_vec, t):
    global pos2D, accel2D
    global pos3D, accel3D
    x, y, z, vx, vy, vz = r_vec
    rE = math.sqrt(x * x + y * y + z * z)    
    rEcubed = rE * rE * rE
    GMe_over_r3 = GMearth / rEcubed
    xM, yM, zM = moonPosition(t)
    xL = x - xM
    yL = y - yM
    zL = z - xM
    rL = math.sqrt(xL * xL + yL * yL + zL * zL)    
    rLcubed = rL * rL * rL
    GMm_over_r3 = GMmoon / rLcubed
    ax = -GMe_over_r3 * x - GMm_over_r3 * xL
    ay = -GMe_over_r3 * y - GMm_over_r3 * yL
    az = -GMe_over_r3 * z
    pos2 = [x, y]
    a2 = [ax, ay]
    pos3 = [x, y, z]
    a3 = [ax, ay, az]
    pos2D = np.append(pos2D, [pos2], axis=0)
    accel2D = np.append(accel2D, [a2], axis=0)
    pos3D = np.append(pos3D, [pos3], axis=0)
    accel3D = np.append(accel3D, [a3], axis=0)
    drdt = [vx, vy, vz, ax, ay, az]
    return drdt

def npmax(l):
    max_idx = np.argmax(l)
    max_val = l[max_idx]
    # return (max_idx, max_val)
    return max_val

def npmin(l):
    min_idx = np.argmin(l)
    min_val = l[min_idx]
    # return (min_idx, min_val)
    return min_val


# if called from command line
if 'cmd' in decoded:
    cmd = decoded['cmd']
    t_1 = 100000
    print moonPosition(t_1)
    r_1 = [0, 10000, 0, 0, 0, 0]
    print acceleration(r_1, t_1)
    sys.exit()


try:
    os.remove("writeFiles/earthMoon02.png")
    os.remove("writeFiles/earthMoon02.csv")
    os.remove("writeFiles/earthMoon02Plot.html")

except Exception: 
    pass

try:
    tarray = np.linspace(t0, t0 + deltat, num=300)
    mx = 300000 * np.sin(m_omega * tarray)
    my = 300000 * np.cos(m_omega * tarray)

    fig = plt.figure()

    ax = fig.add_subplot(111, axisbg='#EEEEEE')
    # ax.grid(color='white', linestyle='solid')

    if central == 'Earth':
        circle1 = plt.Circle((0, 0), 6378, color='#36AFBF')
        plt.gcf().gca().add_artist(circle1)

    plt.plot(mx, my)
   
    plt.xlim(-plotsize, plotsize)
    plt.ylim(-plotsize, plotsize)

    y_vec0 = [x0, y0, 0, vx0, vy0, 0]
    print 'y_vec0 ', y_vec0,

    sol = odeint(acceleration, y_vec0, tarray)
    # print sol
    plt.plot(sol[:, 0], sol[:, 1])    
    plt.gca().set_aspect('equal', adjustable='box')
    plt.draw()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Earth-Moon')
    plt.grid(True)
 
    Path = mpath.Path
    code = (Path.MOVETO, Path.LINETO)    
    mylen = len(pos2D)
    for i in range(0, mylen, 20):
        mynorm = [np.linalg.norm(x) for x in accel2D]
        # print length
        x0 = pos2D[i,0]
        y0 = pos2D[i,1]
        x1 = x0 + 50000 * accel2D[i,0] / mynorm[i]
        y1 = y0 + 50000 * accel2D[i,1] / mynorm[i]
        # print x0,y0,x1,y1
        vert = [(x0, y0), (x1, y1)]
        path = mpath.Path(vert, code)
        patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
        ax.add_patch(patch)

    result_array = np.concatenate((pos3D, accel3D), axis=1)    
    np.savetxt("writeFiles/earthMoon02.csv", result_array, delimiter=",")
    plt.savefig("writeFiles/earthMoon02.png", bbox_inches='tight')
    mpld3.save_html(fig, "writeFiles/earthMoon02Plot.html")
    # mpld3.fig_to_html(fig, template_type="simple")
    # mpld3.show()
    
    
except Exception:
    print(traceback.format_exc())
    print "exception"
    print "end"
