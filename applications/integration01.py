#import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from random import randint
import traceback
import os
from scipy.integrate import odeint



f=randint(0,9)

# ODE      (3x-1)y''-(3x+2)y'-(6x-8)y=0; y(0)=2, y'(0)=3
# solution y=2*exp(2*x)-x*exp(-x)

def g(y, x):
    y0 = y[0]
    y1 = y[1]
    y2 = ((3*x+2)*y1 + (6*x-8)*y0)/(3*x-1)
    return y1, y2








try:
    os.remove("writeFiles/integration01.png")
except Exception: 
    pass


try:

    # Initial conditions on y, y' at x=0
    #init = 2.0, 3.0
    init = f, 3.0
    # First integrate from 0 to 2
    x = np.linspace(0,2,100)
    sol=odeint(g, init, x)
    # Then integrate from 0 to -2
    plt.plot(x, sol[:,0], color='b')
    x = np.linspace(0,-2,100)
    sol=odeint(g, init, x)
    plt.plot(x, sol[:,0], color='b')
    # The analytical answer in red dots
    exact_x = np.linspace(-2,2,10)
    #exact_y = 2*np.exp(2*exact_x)-exact_x*np.exp(-exact_x)
    emx=np.exp(-exact_x)
    e3x=np.exp(3*exact_x)
    exact_y = emx*((3-2*f)*exact_x+f*e3x)
    #exact_y = emx*(3-2*f)*x
    plt.plot(exact_x,exact_y, 'o', color='r', label='exact')
    plt.legend()
    
    
    
    
    
    plt.grid(True)
    plt.savefig("writeFiles/integration01.png", bbox_inches='tight')



except Exception:
    print(traceback.format_exc())
    print "exception"
    print "end"


#matplotlib.style.use('ggplot')
