import numpy as np

X1 = np.array([[0.1, 0.8, 0.1], [0.3, 0.1, 0.6], [0.2, 0.5, 0.3], [0.8, 0.1, 0.1]])

Y1 = np.argmax(X1, axis=0)

print(X1.shape)
print()
print(Y1)
print()

Y2 = np.array([1, 2, 1, 0])
T2 = np.array([1, 2, 0, 0])

X2 = np.sum(Y2==T2)

print(Y2==T2)
print()
print(X2)
print()
