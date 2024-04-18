import numpy as np
import matplotlib.pyplot as plt
n = 101
r = 10
m = 1000
alpha = 0.25  # Puedes ajustar este valor según lo necesites

def create_A_explicit(alpha, n):
    A = np.zeros((n, n))
    for i in range(1, n-1):
        A[i, i] = 1 + 2 * alpha
        A[i, i-1] = -alpha
        A[i, i+1] = -alpha
    A[0, 0] = 1
    A[-1, -1] = 1
    return A

u = np.zeros(n)
u[(n//2 - r):(n//2 + r)] = 1

A = create_A_explicit(alpha, n)
for _ in range(m):
    u = np.dot(A, u)

plt.plot(u)
plt.xlabel('Posición')
plt.ylabel('Valor de u')
plt.title('Evolución de u (Método Explícito)')
plt.show()

def create_A_implicit(alpha, n):
    A = np.zeros((n, n))
    for i in range(1, n-1):
        A[i, i] = 1 + 2 * alpha
        A[i, i-1] = -alpha
        A[i, i+1] = -alpha
    A[0, 0] = 1
    A[0, 1] = -1
    A[-1, -2] = -1
    A[-1, -1] = 1
    return A

u = np.zeros(n)
u[(n//2 - r):(n//2 + r)] = 1

A_implicit = create_A_implicit(alpha, n)
for _ in range(m):
    u = np.linalg.solve(A_implicit, u)

plt.plot(u)
plt.xlabel('Posición')
plt.ylabel('Valor de u')
plt.title('Evolución de u (Método Implícito)')
plt.show()

