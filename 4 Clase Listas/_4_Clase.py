#Listas... se definen con corchetes
auxlist = [1,'hola',1.34, 123]
colores = ["rojo","verde","azul",'amarillo']
números = list((1,2,3,4,5,6,7))
print(números)
print(type(números))
R = list(range(1,50))
print(R)
print(colores)
print(auxlist)
print("--"*30)
#son distintas formas de crear y mostrar una lista
#las listas igual que los string son una clase
#para ver los métodos disponibles de la clase list hago..:
print(dir(colores))
#y veo todos los métodos de la variable tipo lista llamada colores
#ejemplo
print(len(colores))
#las listas son vectores que arrancan en el sbíndice cero
print(colores[1])
print('amarillo' in colores)
print("--"*30)
#puedo hacer
colores[1]= 'violeta'
print(colores)
colores.append("Último color")
print(colores)
#ojo!!! si hago append de dos colores estoy agregando una sublista
#ejemplo
colores.append(["color1",'color2'])
print(colores)
print("--"*30)
#además se pueden insertar elementos en posiciones determinadas
#indicadas por el subíndice, de atrás hacia delante los subíndices son -1 -2... -n
#también se pueden eliminar elementos con método pop (el último) o remove (uno en particular)
print(colores)
colores.remove("Último color")
print(colores)
colores.pop()
colores.sort(reverse = False)  #ordena
print(colores)
print("--"*30)
print("--"*30)

#Listas
print("+"*50)
[10,20,30,50,99]
L1 = ["Hola",4,5.5,'Adiós']
[]  #Lista vacía
print([10,20])
print(type([10,20]))
print("+"*50)

#Tuplas
#son constantes a diferencia de las listas
(10,20,30,40)
print((10,20))
print((10,90))
print(L1[:])  #o print(L1)
#Si mostramos índices negativos comienza da atrás hacia adelante
print(L1[-2]) #muestra 5.5
print(L1[0:3]) #muestra el subrango
print("+"*50)
L1.append('Último')   #agrega al final
print(L1)

print("+"*50)
L1.insert(2,"Intermedio")   #agrega y desplaza los siguientes
print(L1)

print("+"*50)
L1.extend(["Juana","Betiana"])   #agrega al final
print(L1)

print("+"*50)
print(L1.index("Betiana"))   #devuelve pos de la primera coincidencia

print("+"*50)
print('Pepe'in L1)  #si se encuentra pepe en L1

print("+"*50)
L1.remove('Juana')   #Elimina a Juana de L1
L1.pop()  #quita el último elemento
print(L1)

print("+"*50)
L2 = ["Juan","José","Pedro",'Ana','Gabriel',"Beatriz",'Sofía']
L3 = L1+L2    #concatenar listas
print(L3)

print("+"*50)
L2 = L2*3    #multiplica la lista
print(L2)

print("+"*50)
#print(dir(list))

print("+"*50)

#Ejemplo de recorrido de una lista
for i in L2:
    if i[0]=='A' or i[0]=='J':
        print(i)

print("+"*50)

print("+"*50)
