#
# read binary file (tuple)
# and print it
#Juan Francisco Arreola Hernández, arreola_juan@ucol.mx
import pickle

with open('tuple.bin','rb') as fh:
        t = pickle.load(fh) 

print(type(t))
print(t)

print('done...')