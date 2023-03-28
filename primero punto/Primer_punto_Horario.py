# Horario 

clases = ['semiconductores','programacion','magnetismo','circuitosAC','constitucion','ecologia','fundamentos']
Hora_Desde = ['9:00 am', '11:00 am','1:00 pm','3:00 pm' ]
Hora_hasta = ['11:00 am','1:00 pm','3:00 pm','5:00 pm']
profesor = ['Jimi','Nicolas','Lalinde','Bohorquez','Catalina','Julian','Yuberney']
salon = ['303 DB','205 PS','303 GO','406 DB','305 PS','305 DB']


def horario():
    opc = input("¿Que dia decea revisar?:\n")

    if opc == 'lunes':
            cl= clases[4]
            hd= Hora_Desde[3]
            hh=Hora_hasta[3]
            p=profesor[6]
            s=salon[0]
            print(f"su clase es:",cl),print(f"la hora es:",hd,hh),print(f"el profesror es:",p),print(f"su salon es:",s)

        
    elif opc == 'martes':
            pc = clases[0],Hora_Desde[0],Hora_hasta[0],profesor[0],salon[1]
            sc = clases[1],Hora_Desde[2],Hora_hasta[2],profesor[1],salon[2]
            tc = clases[2],Hora_Desde[3],Hora_hasta[3],profesor[2],salon[3]
            print(f"su primera clase es:\n",pc)
            print(f"su segunda clase es:\n",sc)
            print(f"su tercera clase es:\n",tc)
        

    elif opc == 'miercoles':
            cl= clases[3]
            hd= Hora_Desde[3]
            hh=Hora_hasta[3]
            p=profesor[3]
            s=salon[4]
            print(f"su clase es:",cl),print(f"la hora es:",hd,hh),print(f"el profesror es:",p),print(f"su salon es:",s)
        
    elif opc == 'jueves':
            pc = clases[0],Hora_Desde[0],Hora_hasta[0],profesor[0],salon[1]
            sc = clases[1],Hora_Desde[2],Hora_hasta[2],profesor[1],salon[2]
            tc = clases[2],Hora_Desde[3],Hora_hasta[3],profesor[2],salon[3]
            print(f"su primera clase es:\n",pc)
            print(f"su segunda clase es:\n",sc)
            print(f"su tercera clase es:\n",tc)

    elif opc == 'viernes':
            pc = clases[5],Hora_Desde[0],Hora_hasta[0],profesor[4],salon[4]
            sc = clases[6],Hora_Desde[2],Hora_hasta[2],profesor[5],salon[5]
            tc = clases[3],Hora_Desde[3],Hora_hasta[3],profesor[3],salon[4]
            print(f"su primera clase es:\n",pc)
            print(f"su segunda clase es:\n",sc)
            print(f"su tercera clase es:\n",tc)

    
if __name__=='__main__':
    print(horario)


        
       

    
    
        
           
          


    
 