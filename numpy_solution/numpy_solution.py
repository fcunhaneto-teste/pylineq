import numpy as np

"""
Ax = B
"""
A = np.array([[3, -2, 5], [6, -9, 12], [-5, 0, 2]])
B = np.array([20, 51, 1])
c = np.linalg.solve(A, B)
print(c)