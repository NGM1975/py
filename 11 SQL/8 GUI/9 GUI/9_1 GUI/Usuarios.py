#Métodos getters y setters
class Usuarios():
#atributos
    def __init__(self,nombre,passw):
        self.__passw = passw
        self.__nombre = nombre

#-------------------getters---------------------------------
    def getNombre(self):
        return self.__nombre

    def getPassw(self):
        return self.__passw
#------------------setters---------------------
    def setNombre(self,nombre):
        self.__nombre = nombre

    def setPassw(self,passw):
        self.__passw = passw

#---------------Istasación de objetos-------------------------------