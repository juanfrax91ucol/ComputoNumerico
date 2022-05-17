##
#2do
# Metodo 2 - Diferencias finitas centradas,
# Calcular Derivacion numerica 
# sen**3(2x)/x**4+1 
# Juan Francisco Arreola Hernandez.
from math import sin

def f(x):
           #sin**3(2x) = sen(2x)**3 
    return (sin(2*x))**3/((x**4)+1)

x0=2.45

h1=0.5
r1=(f(x0+h1)-f(x0-h1))/(2*h1)
print('r1 = ',r1)

h2=0.1
r2=(f(x0+h2)-f(x0-h2))/(2*h2)
print('r2 = ', r2)

h3=0.001
r3=(f(x0+h3)-f(x0-h3))/(2*h3)
print('r3 = ', r3)