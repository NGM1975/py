#Método constructor con parámetros
class Vehículo():
    #Método constructor de la clas o estado inicial.. "de fábrica"
    def __init__(self,mar,mod,año):
        self.__marca = mar #atributos encapsulados con el __
        self.__modelo = mod #atributos encapsulados con el __
        self.año = año
        self.__estado = False

    def arrancar(self):
        self.__estado = True

    def parar(self):
        self.__estado = False

    def mostrarVehículo(self):
        print(self.__marca)
        print(self.__modelo)
        print(self.año)
        if self.__estado == True:
            print("Este vehículo está en marcha")
        else:
            print("Vehículo parado")