#
# convert 1st variable as tuple
# convert 2nd variable as dictionary
# convert 3rd variable as list
# Juan Francisco Arreola Hernández
#import matplotlib.pyplot as plt

import pandas as pd
iris = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv')


print('head',iris.head())
print(" ")
print("----------> Tuplas - Sepal Length <----------")
print(" ")
print(tuple(iris['sepal length']))
print(" ")
print("----------> Diccionario - Sepal Width <----------")
print(" ")
print(iris['sepal width'].to_dict())
print(" ")
print(" ")
print("----------> Lista - Petal Length <----------")
print(" ")
print(iris['petal length'].to_list())
print(" ")

