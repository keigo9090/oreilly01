import numpy as np

class sigmoid:
    def __init__(self):
        self.out = None

    def forword(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out

        return out
    
    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out

        return dx
    
