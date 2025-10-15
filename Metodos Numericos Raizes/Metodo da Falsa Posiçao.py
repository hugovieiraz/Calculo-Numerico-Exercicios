# metodo da falsa posição 
import numpy as np
a= 0
b = 1
def f(x):
    return x**2 + 2*x - 1
for i in range (0,4,1):
    fxa = f(a)
    fxb = f(b)
    r = b- (fxb*(a-b))/(fxa - fxb)
    fxr = f(r)
    if (fxa*fxr)>0:
        a=r 
    print(f'para o ponto {r} temos o ponto `{fxr}')
