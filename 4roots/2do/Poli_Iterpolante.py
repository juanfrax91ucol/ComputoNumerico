##
#2do
#Polinomio Interpolante, Encontrar el valor de "Y"
# Juan Francisco Arreola Hernandez.

p1 = (2,3)
p2 = (5,-2)
p3 = (6,5)
p4 = (8,-1)

# El usuario ingresará el valor de "X"
def fn(p1,p2,p3,p4):
    x = float(input("Ingresa el valor de X: "))
    r1=(((x-p2[0])*(x-p3[0])*(x-p4[0]))/((p1[0]-p2[0])*(p1[0]-p3[0])*(p1[0]-p4[0])))*(p1[1])
    r2=(((x-p1[0])*(x-p3[0])*(x-p4[0]))/((p2[0]-p1[0])*(p2[0]-p3[0])*(p2[0]-p4[0])))*(p2[1])
    r3=(((x-p1[0])*(x-p2[0])*(x-p4[0]))/((p3[0]-p1[0])*(p3[0]-p2[0])*(p3[0]-p4[0])))*(p3[1])
    r4=(((x-p1[0])*(x-p2[0])*(x-p3[0]))/((p4[0]-p1[0])*(p4[0]-p2[0])*(p4[0]-p3[0])))*(p4[1]) 
    return r1+r2+r3+r4

print("Valor de Y es: ", fn(p1,p2,p3,p4))

