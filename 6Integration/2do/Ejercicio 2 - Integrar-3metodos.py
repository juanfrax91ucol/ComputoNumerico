##
#2do
# 3 Metodos
# Calcular Derivacion numerica 
# (7**-x)+3
# Juan Francisco Arreola Hernandez.

def f(x):
    return (7**-x)+3

a=-1
b=2

m=(a+b)/2 # Se usara nuevamente
r1=f(m)*(b-a)
print('Regla del Punto Medio: ',r1)

r2=(((b-a))/2)*(f(a)+f(b))
print('Regla del Trapecio: ',r2)

r3=((b-a)/6)*(f(a)+4*f(m)+f(b))
print('Regla de Simpson: ',r3)