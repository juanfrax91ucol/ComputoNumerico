#
# radious of circle inscribed in a tringle
# place here your solution code
#
# Juan Francisco Arreola Hernández, arreola_juan@ucol.mx
import math

valA = input ("Ingresa A: ")
a = float(valA)

valB = input ("Ingresa B: ")
b = float(valB)

valC = input ("Ingresa C: ")
c = float(valC)

s = (1/2)*(a+b+c)

r = (math.sqrt(s*(s-a)*(s-b)*(s-c)))/s
print("Valor de s es: ", s)
print("Valor de r es: ", r)