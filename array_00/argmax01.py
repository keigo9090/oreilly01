import numpy as np

A = np.array([0.1, 0.8, 0.1])
B = np.array([0.3, 0.1, 0.6])
C = np.array([0.2, 0.5, 0.3])
D = np.array([0.8, 0.1, 0.1])

E = A*B*C*D

F = np.einsum('i,i,i,i->', A,B,C,D)

G1 = np.dot(np.dot(A,B), np.dot(C,D))
G2 = np.dot(np.dot(A,C), np.dot(B,D))
G3 = np.dot(np.dot(A,D), np.dot(B,C))

print(E)
print()
print(F)
print()
print(G1,G2,G3, sep="\n\n")
print()
