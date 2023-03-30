#MATRIZ
import random
import numpy as np

m = np.random.randint(100,size=(5,10))

print('la matriz es:')
print(m)

maximo = np.max(m)
pmax = np.where(m == max)
minimo = np.min(m)
pmin = np.where(m == min)
print('el numero maximo de la matriz es:',max,'en la posicion',pmax)
print('el numero minimo de la matriz es:',min,'en la posicion',pmin)

matrizorde = np.sort(m,axis = None)[::-1].reshape((5,10))
print('la matriz ordenada es:',matrizorde)










