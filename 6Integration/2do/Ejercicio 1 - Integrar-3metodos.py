##
#2do
# 3 Metodos
# Calcular Derivacion numerica 
# 2sen(sqrt(x))-x 
# Juan Francisco Arreola Hernandez.

from math import sin, sqrt

def f(x):
           #sin**3(2x) = sen(2x)**3 
    return 2*(sin(sqrt(x)))-x

a=0
b=1.9724


m = (a+b)/2 #Se usara de nuevo
r1 = f(m)*(b-a)
print('Regla del Punto Medio: ',r1)

r2 = ((b-a)/2)*(f(a)+f(b))
print('Regla del Trapecio: ',r2)

r3 = ((b-a)/6)*(f(a)+4*f(m)+f(b))
print('Regla de Simpson: ',r3)