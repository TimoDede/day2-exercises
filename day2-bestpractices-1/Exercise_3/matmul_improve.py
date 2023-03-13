# Program to multiply two matrices using nested loops
import random
import numpy as np

N = 250

# NxN Matrix
X = np.random.randint(0, 100, (N, N))
print(X)

# Nx(N+1) matrix
Y = np.random.randint(0, 100, (N, N+1))
print(Y)

# result is Nx(N+1)
result = np.matmul(X, Y)
print(result)