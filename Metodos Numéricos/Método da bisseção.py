#metodo da bisseção
import numpy as np 
xa = 0
xb = 1

def equação(x):
    return (x**2 + 2*x -1)
 
for i in range(0,3,1):
    xc =(xa+xb)/2
    fxa = equação(xa)
    fxb = equação(xb)
    fxc = equação(xc)
    if (fxa*fxc)<0 :
        xb = xc
    else:
        xa=xc

print(xc)