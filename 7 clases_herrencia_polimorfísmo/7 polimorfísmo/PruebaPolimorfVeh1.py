from PolimorfísmoVeh import *

class Concesionaria():
    def __init__(self):
        pass

    def Autos(self):
        print('AUTO')
        print('Ingrese marca, modelo, año y ruedas\n')
        ma = input('Marca? ')
        mo = input('Modelo? ')
        an = int(input('Año? '))
        ru = int(input('Ruedas? '))
        MiCoche = Vehículo(ma,mo,an,ru)
        return MiCoche
    def Camionetas(self):
        print('CAMIONETA')
        print('Ingrese marca, modelo, año, ruedas y carga\n')
        ma = input('Marca? ')
        mo = input('Modelo? ')
        an = int(input('Año? '))
        ru = int(input('Ruedas? '))
        ca = int(input('Carga? '))
        MiCamión = Camioneta(ma,mo,an,ru,ca)
        return MiCamión
    def Motos(self):
        print('MOTO')
        print('Ingrese marca, modelo, año y ruedas\n')
        ma = input('Marca? ')
        mo = input('Modelo? ')
        an = int(input('Año? '))
        ru = int(input('Ruedas? '))
        MiMoto = Moto(ma,mo,an,ru)
        return MiMoto
    def Cuatriciclos(self):
        print('CUATRICICLO')
        print('Ingrese marca, modelo, año, ruedas y cilindrada\n')
        ma = input('Marca? ')
        mo = input('Modelo? ')
        an = int(input('Año? '))
        ru = int(input('Ruedas? '))
        ci = int(input('Cilindrada? '))
        MiCuatri = Cuatriciclo(ma,mo,an,ru,ci)
        return MiCuatri
    def Bicieléctrica(self):
        print('BICI ELÉCTRICA')
        print('Ingrese marca, modelo, año, ruedas, autonomía y rodado\n')
        ma = input('Marca? ')
        mo = input('Modelo? ')
        an = int(input('Año? '))
        ru = int(input('Ruedas? '))
        aut = int(input('Autonomía? '))
        ro = int(input('Rodado? '))
        MiBici = Bicieléctrica(ma,mo,an,ru,aut,ro)
        return MiBici

#---------------------Menú de vehículos---------------------------
    def crearTipoVehículo(self):
        aux = 10
        while(aux < 0 or aux > 7):
            print('-'*70)
            print('\tIndique tipo de vehículo a incorporar: \n')
            print('\t1 para autos (clases vehículo)\n')
            print('\t2 para camioneta\n')
            print('\t3 para motos\n')
            print('\t4 para cuatriciclos\n')
            print('\t5 para vehículos tipo coches esléctricos\n')
            print('\t6 para bicicletas con baterías\n')
            print('\t7 para ver listado de unidades\n')
            print('\t0 para finalizar\n')
            print('-'*70)
            aux = int(input('ingrese una opción: '))
        return aux
#-----Ciclo para crear los distintos tipos de vehículos----------
    def crearUnidades(self):
        Unidades = []
        tipoVeh = 1
        while(tipoVeh != 0):
            print('#'*70)
            tipoVeh = self.crearTipoVehículo()

            if(tipoVeh == 1): #autos
                Unidades.append(self.Autos())
            elif(tipoVeh == 2): #camionetas
                Unidades.append(self.Camionetas())
            elif(tipoVeh == 3): #motos
                Unidades.append(self.Motos())
            elif(tipoVeh == 4): #cuatriciclos
                Unidades.append(self.Cuatriciclos())
            elif(tipoVeh == 6): #bici
                Unidades.append(self.Bicieléctrica())
            elif(tipoVeh == 7):
                self.mostrarUnidades(Unidades)

#----------Muestra de unidades disponibles-------------------
    def mostrarUnidades(self,unid):
        for i in unid:
            print('#'*70)
            i.mostrarVehículo()
            print('#'*70)
        c = input('Pulse una tecla para continuar')
##############################################################
a = Concesionaria()
a.crearUnidades()


#ver instance(objeto,clase)
#ver variables de  clases

