import numpy as np
import matplotlib.pylab as plt

def function_2(x):
    return np.sum(x**2)   #x[0]**2 + x[1]**2     

x = np.arange(0.0, 20.0, 0.1)
y = function_2(x)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(y)
plt.show()
