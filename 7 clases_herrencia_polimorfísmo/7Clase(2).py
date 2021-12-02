#clases definiciones
class Vehículo():
    marca = 'Ford'
    modelo = 'Mondeo'
    año = 2010
    estado = False
    disponible = False

#--------------------------------------
    def arrancar(self):
        self.estado = True

    def parar(self):
        self.estado = False
#-----Método con parámetros-----------
    def habilitar(self, dato):
        self.disponible = dato
#-------------------------------------
    def mostrarVehículo(self):
        print('Marca: ',self.marca)
        print('Modelo: ',self.modelo)
        print('Año Fabricación: ',self.año)
        if self.estado == True:
            print("Este vehículo está en marcha")
        else:
            print("Vehículo parado")
        if self.disponible:
            print("Este vehículo está disponible en salón de ventas")
        else:
            print("Este vehículo NO está disponible en salón de ventas")
#-------------------------------------------
print('-'*50)
V = Vehículo()
V.arrancar()
aux = int(input('Ingrese 1 vehículo disponible 0 si no lo está:  '))
print('-'*50)
V.habilitar(aux)
V.mostrarVehículo()
print('-'*50)

aux = int(input('Ingrese 1 vehículo disponible 0 si no lo está:  '))
print('-'*50)
V.habilitar(aux)
V.parar()
V.mostrarVehículo()
print('-'*50)
print('-'*50)



