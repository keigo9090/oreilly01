import numpy as np

class ReLU:
    def __init__(self):
        self.mask = None

    def forword(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0

        return out
    
    def backforward(self, dout):
        dout[self.mask] = 0
        dx = dout

        return dx
    
# Relu クラスは、インスタンス変数としてmaskという変数を持ちます。
# このmask変数は True/False からなるNumPy配列で、順伝播の入力である✕の要素で0以下の場所をTrue、
# それ以外（0より大きい要素）をFalseとして保持します。
# たとえば、次の例で示すように、True/FalseからなるNumPy配列をmask 変数は保持します。

x = np.array([[1.0, -0.5],[-2.0, 3.0]])
print(x)
print()

mask = (x <= 0)
print(mask)