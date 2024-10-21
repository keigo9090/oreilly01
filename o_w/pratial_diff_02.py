import numpy as np
import matplotlib.pylab as plt

def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)  # 中心差分

def function_2(x):
    return np.sum(x**2, axis=1)  # ベクトル化

# xの範囲を2次元にする
x0 = np.arange(-2, 2, 0.25)
x1 = np.arange(-2, 2, 0.25)
X, Y = np.meshgrid(x0, x1)

# X, Yを結合して一つの配列にする
X = X.flatten()
Y = Y.flatten()

# 関数の値を計算
Z = function_2(np.array([X, Y]).T)

# 3Dプロット
plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X.reshape(X.shape[0]//Y.shape[0], Y.shape[0]), 
                Y.reshape(X.shape[0]//Y.shape[0], Y.shape[0]), 
                Z.reshape(X.shape[0]//Y.shape[0], Y.shape[0]))
plt.show()