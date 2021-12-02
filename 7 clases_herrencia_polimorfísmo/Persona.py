#Métodos getters y setters
class Persona():
    #atributos
    def __init__(self,edad,peso,altura,nombre):
        self.__edad = edad
        self.__peso = peso
        self.__altura = altura
        self.__nombre = nombre
        self.camina = False
        self.lee = False
#------------------------------------------------------
#Métodos
    def caminar(self):
        #print('La persona cambia de posición')
        self.camina = True

    def parar(self):
        #print('La persona no cambia de posición')
        self.camina = False

    def leer(self):
        self.lee = True

    def noleer(self):
        self.lee = False
#-------------------------------------------------------------
    def __estado(self):
        if(self.camina == True):
            if self.lee:
                return 'está caminando y leyendo'
            else:
                return 'está caminando y sin leer'
        else:
            if self.lee:
                return 'está parada y leyendo...'
            else:
                return 'esta parada y sin leer...'
#------------------getters---------------------------------------
    def getNombre(self):
        return self.__nombre

    def getAltura(self):
        return self.__altura

    def getPeso(self):
        return self.__peso

    def getEdad(self):
        return self.__edad
#-----------------setters---------------------------------------
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setAltura(self, altura):
        self.__altura = altura

    def setPeso(self, peso):
        self.__peso = peso

    def setEdad(self, edad):
        self.__edad = edad
#-----------Muestra de una persona------------------------------
    def muestra(self):
        print('-------------------------')
        print('Nombre: ',self.__nombre)
        print('Edad: ',self.__edad)
        print('Altura: ',self.__altura)
        print('Peso: ',self.__peso)
        print(self.__estado())   #acceso al método encapsulado desde
                                  #el interior del objeto
        print('-------------------------')
#------------Instanciación de objetos---------------------------
#---------Ejecución/invocación getters y setters----------------     