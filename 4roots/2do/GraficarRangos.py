
##
#2do
#Generar un range con numeros flotantes y graficarlos,
# Juan Francisco Arreola Hernandez.

#las siguientes 3 lineas son para que el compilador pueda graficar.
import sys
import matplotlib.pyplot as plt
import numpy as np

secuencia = (x/10 for x in range(1, 100)) # definimos hasta que numero generaremos con punto decimal
for x in secuencia:
    px = np.array([5, x]) #Rango de puntos de X
    #print(x, end= " ")
py = np.array([1, 30]) #Rango de puntos de Y
plt.plot(px, py)
plt.show()

#las siguentes dos lineas son para dibujar la gráfica.
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()




