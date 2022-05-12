
##
#2do
#Interpolacion de Newton, Encontrar el valor de "Y"
# Juan Francisco Arreola Hernandez.

p1=(-2,4)
p3=(-1,-2)
p4=(3,5)
p5=(4.3,11)
valX=7.7
x = float(valX)

def fn(x,p1,p3,p4,p5):
    a =(p3[1]-p1[1])/(p3[0]-p1[0])
    b =((p4[1]-p3[1])/(p4[0]-p3[0])-a)/(p4[0]-p1[0])
    c =((((p5[1]-p4[1])/(p5[0]-p4[0]))-((p4[1]-p3[1])/(p4[0]-p3[0])))/(p5[0]-p3[0])-b)/(p5[0]-p1[0])
    return ((p1[1])+(a*(x-p1[0]))+(b*(x-p1[0])*(x-p3[0]))+(c*(x-p1[0])*(x-p3[0])*(x-p4[0])))

print("Cuando X vale 7.7: ")
print("El valor de Y es: ", fn(x,p1,p3,p4,p5))
