import numpy as np 
n= int(input('escolha a dimenção \n'))
np.random.seed(10)
F = np.random.rand(n,n)
G = np.random.rand(n,n)
sumF =0
sumG = 0
for i in range (0,n,1):
    for j in range (0,n,1):
        sumF += (F[i,j])
        sumG += (G[i,j])
uF = (1/n**2)*sumF
uG = (1/n**2)*sumG
print(uF)
print(uG)
