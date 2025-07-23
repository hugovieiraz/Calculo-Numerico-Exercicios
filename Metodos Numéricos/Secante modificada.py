#secante modificada 
x1 = 2
phi = 0.1

i = int(input('selecione o numero de iterações'))

def f(x):
    return (x**2 +2*x -1)

for j in range(0,i,1):
    fx1 = f(x1)
    fphi = f(x1 + phi*x1)
    x_i_mais_um = x1 -(phi*fx1*x1)/(fphi - fx1)
    x1 = x_i_mais_um
    print(f' para a {i} iteração temos a raiz {x_i_mais_um}')
    