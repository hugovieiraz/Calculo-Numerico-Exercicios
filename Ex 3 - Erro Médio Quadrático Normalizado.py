import numpy as np
n = int(input(' escolha a dimenção: \n'))
somaerror=0 
somaF = 0
np.random.seed(10)
F= np.random.rand(n,n)
G= np.random.rand(n,n)

for i in range(0,n,1):
    for j in range (0,n,1):
        somaerror += (F[i,j] -G[i,j])**2
        somaF += F[i,j]**2
EMQ = somaerror/somaF
print(EMQ)