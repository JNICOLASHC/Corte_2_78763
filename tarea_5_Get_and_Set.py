# tarea de getters y setters 

class Ciudadano:
    def __init__(self):
        self__nombre = None
        self__cedula = None
        self__edad = None

    def getNombre(self):
        return self.__nombre
    def getCedula(self):
        return self.__cedula
    def getEdad(self):
        return self.__edad
    
    def setNombre(self,nombre:str):
        self.__nombre = nombre
    def setCedula(self,cedula:int):
        self.__cedula = cedula
    def setEdad(self,edad:int):
        self.__edad = edad
    

    def __parametros(self):
        cedula = 0
        edad = 0
        if cedula>10:
            return str('fuera de rango')
        elif edad >18:
            return str('es mayor de edad')
    
def main():
    persona  = Ciudadano()
    persona.setNombre('Nicolas')
    persona.setCedula(1098815785)
    persona.setEdad(24)
    print(f'su nombre es: {persona.getNombre()}')
    print(f'su cedula es: {persona.getCedula()}')
    print(f'su edad es: {persona.getEdad()}')



if __name__=='__main__':
    main()  



    #-------#------#-----#--------#

    #       Ciudadano 
    #     __Nombre:str
    #     __Cedula:int
    #     __Edad:int

    #      +Ciudadano()
    #      +getNombre():str
    #      +getCedula():int
    #      +getEdad():int

    #     +setNombre(nombre:str)
    #     +setCedula(cedula:int)
    #     +setEdad(edad:int)

    #   -EsMayorDeEdad(edad):mayorEdad
    #   +getEsMayorDeEdad():str


