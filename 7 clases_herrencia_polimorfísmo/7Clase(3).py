#Método constructor y encapsulación de atributos
class Vehículo():
    #Método constructor de la clas o estado inicial.. "de fábrica"
    def __init__(self):
        self.__marca = "Ford" #atributos encapsulados con el __
        self.__modelo = "Mondeo" #atributos encapsulados con el __
        self.año = 2010
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

print("-"*50)
V =Vehículo()
V.arrancar()
V.mostrarVehículo()
print("-"*50)
V.año = 2020 #es válido... se puede
V.__modelo = "Ka"  # no es válido
# V.modelo y V.marca no son accesibles desde afuera
V.mostrarVehículo()
print("-"*50)
V2 = Vehículo()
V2.mostrarVehículo()
print("-"*50)

