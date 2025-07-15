import numpy as np

n = int(input('Escolha a dimensão: '))
np.random.seed(10)

F = np.random.rand(n, n)
G = np.random.rand(n, n)

somaF = 0
somaG = 0

for i in range(n):
    for j in range(n):
        somaF += F[i, j]
        somaG += G[i, j]

uF = somaF / (n ** 2)
uG = somaG / (n ** 2)

soma_DAMF = 0
soma_DAMG = 0

for i in range(n):
    for j in range(n):
        soma_DAMF += abs(F[i, j] - uF)
        soma_DAMG += abs(G[i, j] - uG)

DamF = soma_DAMF / (n ** 2)
DamG = soma_DAMG / (n ** 2)

print(DamF)
print(DamG)