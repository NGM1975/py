#clases definiciones
class Vehículo():
    def __init__(self,marca,modelo,año,ruedas):
        self.__marca = marca
        self.__modelo = modelo
        self.__ruedas = ruedas
        self.__año = año
        self.estado = False
        self.acelerar = False
        self.frenar = False

    def arrancar(self):
        self.estado = True

    def parar(self):
        self.estado = False

    def acelera(self):
        self.frenar = False
        self.acelerar = True

    def frena(self):
        self.frenar = True
        self.acelerar = False

    def mostrarVehículo(self):
        print(self.__marca)
        print(self.__modelo)
        print(self.__año)
        if self.estado:
            print('Este vehículo está en marcha')
        else:
            print('Vehículo parado')
        if self.acelerar:
            print('Este vehículo está acelerando')
        else:
            print('El vehículo está frenado')
###################################################################
class Camioneta(Vehículo):     #herencia simple
    def cargar(self,Kg):
        self.peso = Kg
        if self.peso:
            return 'La camioneta está cargada con' ,self.peso,'Kg'
        else:
            return "La camioneta está vacía..."

####################################################################
print('+'*50)
miCoche = Vehículo("Wolksvagen","Vento",2015,4)
miCoche.mostrarVehículo()
print('+'*50)
miCamioneta = Camioneta('Wolksvagen','Amarok',2016,4)
miCamioneta.mostrarVehículo()
#Elmétodo mostrarVehículo no pertenece a class Furgón...
print('+'*50)
print(miCamioneta.cargar(900))
#El método cargar es própio de la class Furgón
print('+'*50)
miCamioneta.acelera()  #método de la clase padre Vehículo
miCamioneta.mostrarVehículo()
print('+'*50)

        
        