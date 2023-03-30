#funcion recurciva que calcula una funcion 

n = int(input('ingrese el numero:'))

def factorial(n):
    if n == 0 or n == 1:
        return True
    else:
        return n*factorial(n-1)
r = factorial(n)
print(r)





