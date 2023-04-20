

class Ciudadano:

    def __init__(self,nombre:str,documento:int,edad:int):
            self.__Nombre = nombre
            self.__documento = documento
            self.__edad = edad
        
#-----------------Geters------------------------------

    def getNombre(self):
        return self.__Nombre
        
    def getDocumento(self):
        return self.__documento
        
    def getEdad(self):
        return self.__edad
        
 #----------------Setters---------------------------------

    def setNombre(self,nombre:str):
        self.__Nombre = nombre

    def setDocumento(self,documento:int):
        self.__documento = documento

    def setEdad(self,edad:int):
        self.__edad = edad

    #--------sobre carga de metodo--------

    def futbol(self):
        return ("su profecion no a sido avilitada ")

# Ciudadano #1 ( abogado ):


class _Ingeniero(Ciudadano):
    def __init__(self, nombre: str, documento: int, edad: int, proyecto: int, remuneracion: int):
        super().__init__(nombre, documento, edad)

        self.__proyecto = proyecto
        self.__remuneracion = remuneracion

    # ---------------Getters--------------------
    def getProyectos(self):
        return self.__proyecto

    def getRemuneracion(self):
        return self.__remuneracion

    # ---------------Setters--------------------
    def setProyectos(self, proyecto: int):
        self.__proyecto = proyecto

    def setRemuneracion(self, remuneracion: int):
        self.__remuneracion = remuneracion
    
    #     Sobre carga de metos  
    def Empresa(self):
        return ("proyecto completado")
    

# Ciudadano #2 ( Entrenador)

class _Arquitecto(Ciudadano):
    def __init__(self, nombre: str, documento: int, edad: int,obras:int,planos:str):
        super().__init__(nombre, documento, edad)

        self.__obras = obras
        self.__planos = planos

#-------------------Getters------------------

    def getObras(self):
        return self.__obras
    
    def getPlanos(self):
        return self.__planos
    
#-----------------Setters---------------------------

    def setObras(self,obras:int):
        self.__obras = obras

    def setPlanos(self,planos:str):
        self.__planos = planos

#-------------------sobrecarga-------------

    def licitacion(self):
        return ("comienzo de obras  ")

# ciudadano #3 ( Alcalde )

class _Psicologo(Ciudadano):
    def __init__(self, nombre: str, documento: int, edad: int,areas:str,casos:str):
        super().__init__(nombre, documento, edad)

        self.__areas = areas
        self.__casos = casos

#------------------Getters-------------------

    def getAreas(self):
        return self.__areas
    def getCasos(self):
        return self.__casos
    
#---------------Setters----------------------
        
    def setAreas(self,areas):
        self.__areas = areas
    def setCasos(self,casos):
        self.__casos = casos

    def tratamiento(self):
        return ("necesitas tratamiento")




def main():
   
   ingeniero = _Ingeniero("Nicolas", 134256654, 24,26,1500000)

   print("Ingeniero:") 
   print(f"Nombre: {ingeniero.getNombre()}")
   print(f"ID: {ingeniero.getDocumento()}")
   print(f"Edad: {ingeniero.getEdad()}")
   print(f"Proyectos: {ingeniero.getProyectos()}")
   print(f"Remuneracion: {ingeniero.getRemuneracion()}")
   print("")

   arquitecto = _Arquitecto("Pedro",2345654,49,2,"constructora")

   print("Arquitecto")
   print(f"Nombre: {arquitecto.getNombre()}")
   print(f"ID: {arquitecto.getDocumento()}")
   print(f"Edad: {arquitecto.getEdad()}")
   print(f"Obras: {arquitecto.getObras()}")
   print(f"Los planos son: {arquitecto.getPlanos()}")
   print("")

   psicologo = _Psicologo("Marcela",12443555,43,"infantil","Son 7 casos")

   print("El psicologo")
   print(f"Nombre: {psicologo.getNombre()}")
   print(f"ID: {psicologo.getDocumento()}")
   print(f"Edad: {psicologo.getEdad()}")
   print(f"Area: {psicologo.getAreas()} ")
   print(f"Casos: {psicologo.getCasos()}")
   print("")


if __name__ == "__main__":
    main()