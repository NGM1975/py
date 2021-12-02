from Persona import *
print('-'*50)
op = 1
listado = []
while(op):
    print('Ingrese Nombre, edad, altura y peso de la persona')
    nom = input('Ingrese Nombre')
    ed = int(input('Ingrese Edad'))
    alt = float(input('Ingrese Altura'))
    pes = float(input('Ingrese Peso'))
    p = Persona(ed,pes,alt,nom)
    listado.append(p)
    op = int(input('Continúa? 0 = NO'))

print('----------Comenzamos a mostrar listado-----------------')
for i in listado:
    i.muestra()

print('-'*50)
