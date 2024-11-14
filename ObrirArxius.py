import csv
import numpy as np

#Obrir arxius en CSV 
with open('/home/itibcn/Desktop/MachineLearningClassic/Practica/IntroNumpy/Iris.csv', newline='') as archivo:
    lector = csv.reader(archivo)
    llista = []

    for fila in lector:
        llista.append(fila)
    #print(type(llista))

    for element in llista:
        print(element)



#Obrir arxius per default
ficher = open('/home/itibcn/Desktop/MachineLearningClassic/Practica/IntroNumpy/Iris.csv')
print(ficher.read())



#Obrir arxius amb numpy
data = np.genfromtxt('Practica/IntroNumpy/Iris.csv', delimiter=',', skip_header=1, dtype=None, encoding=None)

llistanp = []

for x in data:
    llistanp.append(x)

for element in llistanp:
    print(element)
