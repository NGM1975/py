from PolimorfísmoVeh import *
concesionaria = []
tipoVeh = 1
#-----------------------Menú seleccionador oopción-----------------
def crearTipoVehículo():
    aux = -1
    while(aux < 0 or aux > 6):
        print('-'*70)
        print('\tIndique tipo de vehículo a incorporar: \n')
        print('\t1 para coches (clases vehículo)\n')
        print('\t2 para camioneta\n')
        print('\t3 para motos\n')
        print('\t4 para cuatriciclos\n')
        print('\t5 para vehículos tipo coches esléctricos\n')
        print('\t6 para bicicletas con baterías\n')
        print('\t0 para finalizar\n')
        print('-'*70)
        aux = int(input('ingrese una opción: '))
    return aux
#--------------------Ciclo para crear los distintos tipos de vehículos--------------------------
while(tipoVeh != 0):
    print('#'*70)
    #global concesionaria
    tipoVeh = crearTipoVehículo()

    if(tipoVeh == 1): #coches
        print('AUTO')
        print('Ingrese marca, modelo, año y ruedas\n')
        ma = input('Marca? ')
        mo = input('Modelo? ')
        an = int(input('Año? '))
        ru = int(input('Ruedas? '))
        MiCoche = Vehículo(ma,mo,an,ru)
        concesionaria.append(MiCoche)
    elif(tipoVeh == 2):  #camionetas
        print('CAMIONETA')
        print('Ingrese marca, modelo, año, ruedas y carga\n')
        ma = input('Marca? ')
        mo = input('Modelo? ')
        an = int(input('Año? '))
        ru = int(input('Ruedas? '))
        ca = int(input('Carga? '))
        MiCamión = Camioneta(ma,mo,an,ru,ca)
        concesionaria.append(MiCamión)
    elif(tipoVeh == 3):  #Motos
        print('MOTO')
        print('Ingrese marca, modelo, año y ruedas\n')
        ma = input('Marca? ')
        mo = input('Modelo? ')
        an = int(input('Año? '))
        ru = int(input('Ruedas? '))
        MiMoto = Moto(ma,mo,an,ru)
        concesionaria.append(MiMoto)
    elif(tipoVeh == 4):  #Cuatriciclos
        print('CUATRICICLO')
        print('Ingrese marca, modelo, año, ruedas y cilindrada\n')
        ma = input('Marca? ')
        mo = input('Modelo? ')
        an = int(input('Año? '))
        ru = int(input('Ruedas? '))
        ci = int(input('Cilindrada? '))
        MiCuatri = Cuatriciclo(ma,mo,an,ru,ci)
        concesionaria.append(MiCuatri)
    #elif(tipoVeh == 5):  #Vehículo eléctrico
    #   print('VEHÍCULO ELÉCTRICO')
    #    print('Ingrese marca, modelo, año, ruedas y autonomía\n')  
    #    ma = input('Marca? ')
    #    mo = input('Modelo? ')
    #    an = int(input('Año? '))
    #    ru = int(input('Ruedas? '))
    #    aut = int(input('Autonomía? '))
    #    MiVelec = Veléctricos()
    #    concesionaria.append(MiVelec)
    elif(tipoVeh == 6):  #Bicicletas
        print('BICI ELÉCTRICA')
        print('Ingrese marca, modelo, año, ruedas, autonomía y rodado\n')
        ma = input('Marca? ')
        mo = input('Modelo? ')
        an = int(input('Año? '))
        ru = int(input('Ruedas? '))
        aut = int(input('Autonomía? '))
        ro = int(input('Rodado? '))
        MiBici = Bicieléctrica(ma,mo,an,ru,aut,ro)
        concesionaria.append(MiBici)
#-----------------Muestra de la listra de objetos con polimorfísmo------
print('#'*70)

for i in concesionaria:
    print('#'*70)
    i.mostrarVehículo()

print('#'*70)

#Ver insistance(objeto,clase)

#-------------------------------------------------------------------






