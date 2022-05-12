#
# read binary file (dictionary)
# and print it
#Juan Francisco Arreola Hernández, arreola_juan@ucol.mx
import pickle

with open('dict.bin','rb') as fh:
        d = pickle.load(fh) 

print(type(d))
print(d)

print('done...')
