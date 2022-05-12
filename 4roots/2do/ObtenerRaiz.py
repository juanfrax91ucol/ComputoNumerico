
##
#2do
#Generar un range con numeros flotantes y graficarlos,
# Juan Francisco Arreola Hernandez.
#  Obtener la raiz de la funcion e^(2-x)-7x=0
#

from math import exp
from re import X

def fn(x):
    return exp(2-x)-7*(x)

def f2(x):
    return -exp(2-x)/-7

x0 = 1.055
x1 = -exp(2-x0)/-7

print("X1 = ",x1)

x2 = -exp(2-x1)/-7
print('x2 = ',x2)

x3 = -exp(2-x2)/-7
print("x3 = ",x3)

x4 = -exp(2-x3)/-7
print("x4 = ",x4)

x5 = -exp(2-x4)/-7
print("x5 = ",x5)

x6 = -exp(2-x5)/-7
print("x6 = ",x6)


print('La raiz de e^(2-x)-7x=0 es:  ',x6)