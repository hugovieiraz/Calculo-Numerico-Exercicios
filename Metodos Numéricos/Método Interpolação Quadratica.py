#interpolação quadratica 
# fx1 > fx0 e fx2, aponta pro maximo, cc aponta para o minimo 
import math
x0 =0
x1 =1
x2 =4
ref = 1.4275483
tol = 10**-5
erro_rel =1
def f(x):
    y = 2*math.sin(x)- (x**2/10)
    return y

it = int(input('selecione a iteração'))
#para while
# while (erro_rel >tol):
for i in range(0,it,1):
    fx0 = f(x0)
    fx1 = f(x1)
    fx2 = f(x2)
    numerador = fx0*((x1**2)-(x2**2))+fx1*((x2**2)-(x0**2))+fx2*((x0**2)-(x1**2))
    denominador = (2*fx0*(x1-x2))+(2*fx1*(x2-x0))+(2*fx2*(x0-x1))
    xq = numerador/denominador
    erro_rel = abs(ref-xq)/abs(ref)
    if(xq<x1):
        x2=x1
        x1=xq
    else:
        x0 = x1
        x1 = xq
print(xq)