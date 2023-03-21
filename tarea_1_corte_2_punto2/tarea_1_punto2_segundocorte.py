# calcular seno coseno tangente y logaritmo natural 

import math


def funciones():
    print("seleccione la funcion:\n","seno opc 1:\n","coseno opc 2:\n","tangente opc 3:\n","exp opc 4:\n","log nat opc 5:\n")

    opc = int(input("Ingrese un numero:\n"))
    v = float(input("ingrese un numero:\n"))
    if opc == 1:
        r = math.sin(v)
        print(r)
    elif opc == 2:
        r == math.cos(v)
    elif opc == 3:
        r = math.tan(v)
    elif opc == 4:
        r = math.exp(v)
    elif opc == 5:
        r = math.log(v)

funciones()