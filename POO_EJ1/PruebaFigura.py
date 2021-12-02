from Figura import *
from Triángulo import *
from Cuadrado import *
from Rectángulo import *
from Círculo import *
Geomet = []
tipoFig = 1
def crearTipoFig():
    aux = -1
    while(aux < 0 or aux > 5):
        print('-'*70)
        print('\tElija la figura: \n')
        print('\t1 para figura\n')
        print('\t2 para triángulo\n')
        print('\t3 para cuadrado\n')
        print('\t4 para rectángulo\n')
        print('\t5 para circulo\n')
        print('\t0 para finalizar\n')
        print('-'*70)
        aux = int(input('ingrese una opción: '))
    return aux

while(tipoFig != 0):
    print('#'*70)
    tipoFig = crearTipoFig()

    if(tipoFig == 1): 
        print('FIGURA')
        print('Ingrese nombre y color\n')
        no = input('NOMBRE: ')
        col = input('COLOR: ')
        MiFig = Figura(no,col)
        Geomet.append(MiFig)
    elif(tipoFig == 2): 
#        print('TRIÁNGULO')
        print('Ingrese nombre, color, base, altura y lados\n')
        no = input('NOMBRE: ')
        col = input('COLOR: ')
        b = float(input('BASE: '))
        h = float(input('ALTURA: '))
        l2 =float(input('Lado2: '))
        l3 =float(input('Lado3: '))
        MiTri = Triángulo(no,col,b,h,l2,l3)
        Geomet.append(MiTri)
    elif(tipoFig == 3): 
#        print('CUADRADO')
        print('Ingrese nombre, color y lado\n')
        no = input('NOMBRE: ')
        col = input('COLOR: ')
        ld = float(input('LADO: '))
        MiCuadro = Cuadrado(no,col,ld)
        Geomet.append(MiCuadro)
    elif(tipoFig == 4): 
#        print('RECTÁNGULO')
        print('Ingrese nombre, color y lados\n')
        no = input('NOMBRE: ')
        col = input('COLOR: ')
        b = float(input('LADO 1: '))
        h = float(input('LADO 2: '))
        MiRect = Rectángulo(no,col,b,h)
        Geomet.append(MiRect)
    elif(tipoFig == 5): 
#        print('CIRCULO')
        print('Ingrese nombre, color,radio\n')
        no = input('NOMBRE: ')
        col = input('COLOR: ')
        r = float(input('RADIO: '))
        MiCir = Círculo(no,col,r)
        Geomet.append(MiCir)

print('#'*70)

for i in Geomet:
    print('#'*70)
    i.mostrarFigura()

print('#'*70)