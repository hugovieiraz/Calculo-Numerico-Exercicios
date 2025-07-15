#Erro Médio Quadrático

import numpy as np

n = int(input('escolha a dimenção da matriiz \n'))
somaEMA = 0
np.random.seed(10)
F= np.random.rand(n,n)
G = np.random.rand(n,n)
for i in range(0,n,1):
    for j in range(0,n,1):
        somaEMA += np.abs(F[i,j]-G[i,j])**2
sol = (1/n**2)*somaEMA
print(sol)