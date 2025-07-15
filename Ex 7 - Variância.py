import numpy as np
n= int(input('dimenção de n: \n'))
np.random.seed(10)
F = np.random.rand(n, n)
G = np.random.rand(n, n)

somaF = 0
somaG = 0

for i in range(n):
    for j in range(n):
        somaF += F[i, j]
        somaG += G[i, j]
uF = somaF/n**2
uG = somaG/n**2

sigmaF = 0
sigmaG =0

for i in range(n):
    for j in range(n):
        sigmaF += (F[i, j] - uF)**2
        sigmaG += (G[i, j] - uG)**2
variF = sigmaF/n**2
variG = sigmaG/n**2

print(variF)
print(variG)