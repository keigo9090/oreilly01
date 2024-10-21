import numpy as np

def tanh(x):
    return np.tanh(x)

def tanh_dx(x):
    return 4 / ((np.exp(x) + np.exp(-x))**2)