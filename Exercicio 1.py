import numpy as np
#Considere duas matrizes quadradas F[i, j] e G[i, j], onde
#i, j ∈ {1,2,...,n}. Crie duas matrizes F e G de ordem n×n,
#preenchidas com números aleatórios gerados por uma distri-
#buição uniforme no intervalo [0,1). Finalmente, escreva um
#programa em Python para calcular o Erro Médio Abso-
#luto (EMA) entre essas duas matrizes. O EMA é definido
#como a média das diferenças absolutas entre os elementos
#correspondentes de F e G, conforme a equação
n= int(input('choice the dimention \n'))
np.random.seed(10)
soma_EMA = 0
F = np.random.rand(n,n)
G = np.random.rand(n,n)
for i in range (0,n,1):
    for j in range (0,n,1):
        soma_EMA += np.abs(F[i,j]- G[i,j])
        
sol = (1/n**2)*soma_EMA
print(F)
print(G)
print(sol)