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

m_period = 27.321661547 * 86400
m_omega = 2 * np.pi / m_period
result_array_pos = np.empty((0, 3))
result_array_a = np.empty((0, 3))


# print 'Argument List:', str(sys.argv)
# print sys.argv[1:2]
# print sys.argv[1]
data = sys.argv[1:2]
decoded = json.loads(sys.argv[1])
# print decoded
# print decoded['x0']
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


def moonPosition(t):    
    mx = 300000 * np.sin(m_omega * t)
    my = 300000 * np.cos(m_omega * t)
    mz = 0
    mr = [mx, my, mz]
    return mr    
    
def acceleration(r_vec, t):
    global result_array_pos,result_array_a
    x, y, z, vx, vy, vz = r_vec
    rE = math.sqrt(x * x + y * y + z * z)    
    rEcubed = rE * rE * rE
    # GMe_over_r3 = -1.0 * GMearth / rcubed
    GMe_over_r3 = GMearth / rEcubed
    # print r
    xM, yM, zM = moonPosition(t)
    # xL=xM-x
    # yL=yM-y
    # zL=xM-z
    xL = x - xM
    yL = y - yM
    zL = z - xM
    rL = math.sqrt(xL * xL + yL * yL + zL * zL)    
    rLcubed = rL * rL * rL
    GMm_over_r3 = GMmoon / rLcubed
    ax = -GMe_over_r3 * x - GMm_over_r3 * xL
    ay = -GMe_over_r3 * y - GMm_over_r3 * yL
    az = -GMe_over_r3 * z
    pos = [x, y, z]
    a = [ax, ay, az]
    # f = [x, y, z, ax, ay, az]
    result_array_pos = np.append(result_array_pos, [pos], axis=0)
    result_array_a = np.append(result_array_a, [a], axis=0)
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
except Exception: 
    pass

try:

    # t = np.arange(0.0, 2.0, 0.01)
    
    tarray = np.linspace(t0, t0 + deltat, num=100)
    # print tarray
    mx = 300000 * np.sin(m_omega * tarray)
    my = 300000 * np.cos(m_omega * tarray)
    # print t
    # print mx
    
    # mr=moonPosition(20000)
    # print mr

    fig = plt.figure()


    if central == 'Earth':
        circle1 = plt.Circle((0, 0), 6378, color='#36AFBF')
        # 77 182 196
        plt.gcf().gca().add_artist(circle1)

    # plt.plot(sol[:, 0], sol[:, 1])

    # plt.plot(t,mx)
    plt.plot(mx, my)

    
    # ps1=npmax(sol[:, 0])
    # ps2=np.absolute(npmin(sol[:, 0]))
    # ps3=npmax(sol[:, 1])
    # ps4=np.absolute(npmin(sol[:, 1]))
    # print max(ps1,ps2,ps3,ps4)
    # plotsize=1.01*max(ps1,ps2,ps3,ps4)    
    # plt.xlim(-plotsize, plotsize)
    # plt.ylim(-plotsize, plotsize)
    
    # fit plot into window
    # plotsize=1.01*300000    
    # plotsize=1.2*300000    
    plotsize = 20000    
    
    
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
    # plt.savefig("writeFiles/earthMoon02.png", bbox_inches='tight')
    
    
    mpld3.save_html(fig, "writeFiles/earthMoon02Plot.html")
    mpld3.fig_to_html(fig, template_type="simple")
    # mpld3.show()
    
    # print result_array
    result_array_a *= 1000.0 / result_array_a.max()
    result_array = np.concatenate((result_array_pos, result_array_a),axis=1)
    np.savetxt("writeFiles/earthMoon02.csv", result_array, delimiter=",")

    
except Exception:
    print(traceback.format_exc())
    print "exception"
    print "end"
