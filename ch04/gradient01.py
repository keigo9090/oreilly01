import numpy as np

def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)     # xと同じ形状の配列を生成

    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = tmp_val + h    # f(x+h)の計算
        fxh1 = f(x)

        x[idx] = tmp_val - h    # f(x-h)の計算
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val        #値を元に戻す

    return grad