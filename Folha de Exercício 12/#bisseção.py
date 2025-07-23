#bisseção 
import math 
a = 0
b = 1

def f(x):
    return math.exp**(-x) -x
 
for i in range(0,4,1):
    
    fa = f(a)
    fb = f(b)
    r =b - ((fb*(a-b)))/(fa-fb)
    fr =f(r)
    if (fa*fr) >0 :
        a = r
    else:
        b = r
    print(f'para a {i} iteração a raiz aproximada é {r:.5f}')
