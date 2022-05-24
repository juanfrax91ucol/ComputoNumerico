#
# produce 10,000 coin flips
#
# print how many of them were:
# heads
# tails
#Juan Francico Arreola Hernández.
import random

resultados ={'sello': 0,'cara': 0}

lados=list(resultados.keys())

for _ in range(10000):
    resultados[random.choice(lados)] += 1
print('En 10,000 Volados salieron: ')
print('Sellos: ', resultados['sello'])
print('Caras: ', resultados['cara'])