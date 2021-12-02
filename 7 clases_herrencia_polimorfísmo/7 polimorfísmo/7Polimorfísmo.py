class Coche():
    def desplazamiento(self):
        print("Ando en 4 ruedas")


class Moto():
    def desplazamiento(self):
        print("Amdo en 2 ruedas")


class Camión():
    def desplazamiento(self):
        print('Ando en 10 ruedas')

#MiVehículo1 = Moto()
#MiVehículo1.desplazamiento()
#MiVehículo2 = Coche()
#MiVehículo2.desplazamiento()
#MiVehículo3 = Camión()
#MiVehículo3.desplazamiento()

#FUNCIÓN QUE RECIBE UN OBJETO Y EJECUTA UN MÉTODO
def movimientoVehículo(vehículo):   #Se reemp`laza por el objeto conel que sea llamado
    vehículo.desplazamiento()

miVehículo = Camión()

movimientoVehículo(miVehículo)
#No es necesario indicar de que  tipo es miVehículo OJO!!
#MiVehículo podría ser de cualquiera de las 3 clases

miVehículo1 = Moto()

movimientoVehículo(miVehículo1)


