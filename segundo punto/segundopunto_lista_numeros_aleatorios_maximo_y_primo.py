# numeros aleatorios, numeros maxor y primo 

import random

lista = [random.randint(10,50)for i in range(10)]
print(lista)

def mayor():
        mayor = lista[0]
        for i in range (1,len(lista)):
            if  lista[i] > mayor:
                mayor = lista[i]
                print(mayor)
def nprimo(n):
    if n <= 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False 
        return True
    nprimo = []
    for n in lista:
          if nprimo(n):
            nprimo.append(n)
            print(nprimo)
    else:
        print('no hay numeros primos')

mayor()








                    

            




        

