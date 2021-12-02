
#Se definen entre paréntesis
#Las tuplas tienen menos métodos que las listas por que son CONSTANTES
#Tuplas... son más rápidas que las listas
#ejemplo
print('*'*50)
x = (1,2,3,4)
print(x)
print(type(x))
#pertenece a la clase Tuple y tiene sus métodos
print(dir(x))
#creación
meses = ('enero','febrero',"marzo")
#utilizando constructores
días = tuple(('lunes',"martes",'miércoles',"jueves",'viernes'))
#los índices son iguales a las listas o arrays
print('*'*50)
print(días)
#para definir tuplas de un solo elemento hay que poner coma luego del mismo
#del(días)   #elimina toda la variable
#una tupla puede formar parte de un elemento del tipo diccionario
#ejemplo
ciudades ={
    (4000,5703):'Mar del Plata',
    (4104,5803):'Bahía Blanca'
    }
print(ciudades)
print('*'*50)
for i in días:
    print(i)
    if i[0]=='l':
        print("No creo que sea un buen día\n")
    if len(i)>=7:
        print("Tampoco será bueno\n")

print('*'*50)
#Son listas constantyes
#Son más rígidas y permiten menos métodos
#como extraer una porción de la tupla
print('*'*50)
miTupla = (12,80,12,"Juan","Mar del Plata")
print(miTupla[4], miTupla[2])
print('*'*50)
miLista = list(miTupla)
print(miLista)
print(miTupla)
print('*'*50)

print("Mar del Plata"in miTupla)
print("Balcarce"in miTupla)

print('*'*50)
#Método COUNT()
print('El 12 está: ',miTupla.count(12)," Veces")

#MétodoLEN()
print("La tupla tiene: ", len(miTupla)," Elementos")

print('*'*50)
#Tupla unitaria
T1 = ('Pedro',)
print(T1)
print("La tupla tiene: ", len(T1)," Elementos")
#La coma es obligatoria... de lo contrario tendrá 5 elementos
print('*'*50)
#También la tupla puede no tener paréntesis
T2 = "Lunes","Martes","Miércoles"
print(T2)
día1,día2,día3 = T2
print(día1,día2,día3)

print('*'*50)



