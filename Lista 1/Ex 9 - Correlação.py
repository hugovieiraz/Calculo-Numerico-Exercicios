import numpy as np
n= int(input('dimenção de n: \n'))
np.random.seed(10)
F = np.random.rand(n,n)
G = np.random.rand(n,n)
somaF = 0
somaG = 0
for i in range(0,n,1):
    for j in range(0,n,1):
        somaF += F[i,j]
        somaG += G[i,j]
uF = somaF/n**2
uG = somaG/n**2
covFG = 0

for i in range(0,n,1):
    for j in range(0,n,1):
        covFG += (F[i,j] -uF)*(G[i,j] -uG)
        
cov_total_FG = covFG/n**2
print(cov_total_FG)
