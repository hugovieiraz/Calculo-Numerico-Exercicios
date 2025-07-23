import numpy as np
soma = 0
n = int(input('informe o numero de interações:  '))
erro = 1 
valor_real = 1.082323
def serie(n):
    return 1/(n**4)
for i in range(1,n,1):
    termo_atual = serie(i)
    soma += termo_atual
    erro_relativo = abs(valor_real - soma)/(valor_real)
    print(f'o erro pra a {i} iteração é {erro_relativo}')