from  Vehículo import *
print("-"*50)
#------Un coche-------------------
V = Vehículo("Citroen","C4",2019)
V.mostrarVehículo()
print("-"*50)
#-------Otro coche----------------
V1 = Vehículo("Fiat","Brava",2009)
V1.arrancar()
V1.mostrarVehículo()
print("-"*50)

V1.año = 2020 #es válido.....se puede
V1.__modelo = "Ka"  # no es válido

V1.mostrarVehículo()
print("-"*50)
V2 = Vehículo('Honda','City',2014)
V2.mostrarVehículo()
print("-"*50)