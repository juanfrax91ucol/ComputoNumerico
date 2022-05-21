#
# produce 10,000 coin flips
#
# print how many of them were:
# heads
# tails
#Juan Francico Arreola Hernández.
from random import choice
import random

def volados():
    tiradas = [random.randint(1,2) for i in range(10000)]
    aguila = tiradas.count(1)
    sello = tiradas.count(2)

    print('Águila: ', aguiara, ' y Sello: ', sello)

volados()