#Métodos getters y setters
class Persona():
#atributos
    def __init__(self,nombre,apellido,dirección,passw):
        self.__passw = passw
        self.__dirección = dirección
        self.__apellido = apellido
        self.__nombre = nombre
        self.habilitado = True

#----------------------------------------------------------
    def __baja(self):
        if self.habilitado == True:
            return 'esta persona está habilitada'
        else:
            return 'esta persona no está habilitada'

#-------------------getters---------------------------------
    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getDirección(self):
        return self.__dirección

    def getPassw(self):
        return self.__passw
#------------------setters---------------------
    def setNombre(self,nombre):
        self.__nombre = nombre
    
    def setApellido(self,apellido):
        self.__apellido = apellido

    def setDirección(self,dirección):
        self.__dirección = dirección

    def setPassw(self,passw):
        self.__passw = passw

#---------------Istasación de objetos-------------------------------