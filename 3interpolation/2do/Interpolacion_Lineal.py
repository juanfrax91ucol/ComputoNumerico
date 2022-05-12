#
#2do
#Interpolacion Lineal: Encontrar el valor de "X"
# Juan Francisco Arreola Hernandez.

p1=(-4,-2)
p3=(1,5)

def fn(y,p1,p3):
    a=(p3[0]-p1[0])/(p3[1]-p1[1])
    b=y-p1[1]
    return a*b+p1[0]

#"Y"=3.7
print("Cuando Y vale 3.7: ")
print("El valor de X es: ", fn(3.7,p1,p3))