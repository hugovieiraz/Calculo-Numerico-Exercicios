# Questão 3 prova 2024.2
# verção mais simples
import numpy as np
import math


x = float(input('valor de x: '))
erro_rela_min = float(input(' valor do erro :'))

erro_min = 1
n = 0
soma = 0

valor_verdadeiro = math.sin(x)
def f(n,x):
    return (((-1)**n)/math.factorial(2*n+1))*x**(2*n+1)

while erro_min > erro_rela_min:
    aprox_atual = f(n, x)
    soma += aprox_atual
    erro_calculado = abs((valor_verdadeiro - soma) / valor_verdadeiro)
    erro_min = erro_calculado
    print(n+1, erro_calculado, soma)
    n = n + 1
