from Usuario import *
from Particular import *
from Profesional import *
from Comercial import *

class RegUsuario():
    def __init__(self):
        pass

    def Users(self):
        print('USUARIO')
        print('Ingrese nombre, dirección\n')
        nom = input('NOMBRE: ')
        dire = input('DIRECCIÓN: ')
#        baja = int(input('BAJA SÍ(1)/NO(0): '))
#        ab = int(input('PLAN (Abono 1,2 o 3): '))
#        pul = int(input('PULSOS: '))
        Elusuario = Usuario(nom,dire)
        return Elusuario
    def Particular(self):
        print('PARTICULAR')
        print('Ingrese nombre, dirección, pulsos, dni, fecha de nacimiento\n')
        nom = input('NOMBRE: ')
        dire = input('DIRECCIÓN: ')
        ab = 300
        pul = int(input('PULSOS: '))
        dni = int(input('DNI: '))
        fn = input('FECHA DE NACIMIENTO(año/mes/día): ')
        ElParticular = Particular(nom,dire,ab,pul,dni,fn)
        return ElParticular
    def Profesional(self):
        print('PROFESIONAL')
        print('Ingrese nombre, dirección, pulsos, área, título\n')
        nom = input('NOMBRE: ')
        dire = input('DIRECCIÓN: ')
        ab = 500
        pul = int(input('PULSOS: '))
        ar = input('ÁREA: ')
        ti = input('TÍTULO: ')
        ElProfesional = Profesional(nom,dire,ab,pul,ar,ti)
        return ElProfesional
    def Comercial(self):
        print('COMERCIAL')
        print('Ingrese nombre, dirección, pulsos, rubro, cuit')
        nom = input('NOMBRE: ')
        dire = input('DIRECCIÓN: ')
        ab = 500
        pul = int(input('PULSOS: '))
        ru = input('RUBRO: ')
        cu = input('CUIT: ')
        ElComercial = Comercial(nom,dire,ab,pul,ru,cu)
        return ElComercial    


    def crearTipoUsuario(self):
        aux = 10
        while(aux < 0 or aux > 5):
            print('-'*70)
            print('\tIndique categoría de usuario: \n')
            print('\t1 Usuario\n')
            print('\t2 Particular\n')
            print('\t3 Profesional\n')
            print('\t4 Comercial\n')
            print('\t5 para ver listado de usuarios\n')
            print('\t0 para finalizar\n')
            print('-'*70)
            aux = int(input('ingrese una opción: '))
        return aux

    def crearUsuarios(self):
        Registro = []
        tipoUs = 1
        while(tipoUs != 0):
            print('#'*70)
            tipoUs = self.crearTipoUsuario()

            if(tipoUs == 1): 
                Registro.append(self.Users())
            elif(tipoUs == 2): 
                Registro.append(self.Particular())
            elif(tipoUs == 3): 
                Registro.append(self.Profesional())
            elif(tipoUs == 4): 
                Registro.append(self.Comercial())
            elif(tipoUs == 5):
                self.mostrarRegistro(Registro)


    def mostrarRegistro(self,reg):
        for i in reg:
            print('#'*70)
            i.mostrarUsuario()
            print('#'*70)
        c = input('Pulse una tecla para continuar')

a = RegUsuario()
a.crearUsuarios()