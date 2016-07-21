#import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from random import randint
import traceback
import os

f=randint(0,9)

t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2*f*np.pi*t)


print 7



try:
    os.remove("writeFiles/pic01.png")
except Exception: 
    pass


try:
    plt.plot(t, s)    
    print 8
    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('Sine')
    plt.grid(True)



    #plt.savefig("test.png")
    #plt.show()
    plt.savefig("writeFiles/pic01.png", bbox_inches='tight')
except Exception:
    print(traceback.format_exc())
    print "exception"
    print "end"


#matplotlib.style.use('ggplot')
