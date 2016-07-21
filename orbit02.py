#import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2*np.pi*t)


print 7

try:
    plt.plot(t, s)    
    print 8
    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('About as simple as it gets, folks')
    plt.grid(True)



    #plt.savefig("test.png")
    #plt.show()
    plt.savefig("writeFiles/pic01.png", bbox_inches='tight')
except Exception:
    print(traceback.format_exc())
    print "exception"
    print "end"


#matplotlib.style.use('ggplot')
