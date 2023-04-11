#presio con y sin iva 


def main ():

        f=open('Alimentos.txt','rt')
        m = f.readline()
        f.seek(0)
        lista =[]
        

        for i in range(len(m)):
            producto = f.readline().rstrip('\n').split(',')
            lista.append(producto)
            print(producto)

        while True:
             p = str(input('ingrese un producto o escriba salir para terminar el progrma:\n'))
             if p == 'salir':
                  break
             ValorNeto = float(input('ingrese el valor neto del producto:\n'))

             for lista in lista:
                  if lista == p:
                       ValorInicial = ValorNeto (1 + lista[1])
                       ValorIva = float(lista[p][1])

                       print(f'El valor inicial del producto es: {ValorInicial}')
                       print(f'El valor con IVA es: {ValorIva:2f}')
                       print(f'El valor neto es:{ValorNeto}')



if __name__=='__main__':
    main()