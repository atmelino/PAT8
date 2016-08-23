import matplotlib.pyplot as plt
import numpy as np

# Trial function for adding vertical arrows to
def f(x):
    return np.sin(2*x)

x = np.linspace(0,10,1000)
y = f(x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y, 'k', lw=2)
ax.set_ylim(-3,3)

def add_force(F, x1):
    """Add a vertical force arrow F pixels long at x1 (in data coordinates)."""
    ax.annotate('', xy=(x1, f(x1)), xytext=(0, F), textcoords='offset points',
                arrowprops=dict(arrowstyle='<|-', color='r'))

add_force(60, 4.5)
add_force(-45, 6.5)

plt.show()
