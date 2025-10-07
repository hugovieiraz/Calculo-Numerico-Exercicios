#metodo da secante
import numpy as np 

x1 = 1
x0 = 1.5

i = int(input(' digite o numero de iterações '))

def f(x):
    return (x**2 + 2*x -1)

for j in range (0,i,1):
    fx1 = f(x1)
    fx0 = f(x0)
    x_i_mais_um = x1 - (fx1*(x0-x1))/(fx0-fx1)
    x0 = x1
    x1 = x_i_mais_um
    print(f'para a iteração {j} temos a raiz {x_i_mais_um}')