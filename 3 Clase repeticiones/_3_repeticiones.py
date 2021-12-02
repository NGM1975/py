#CICLO WHILE
contador = 0
print('--'*30)
print('Iniciando.....')
while contador < 5:
    print('Cuerpo ',contador,',', end='')     #Cuerpo del ciclo while
    contador = contador+1                #sigue el cuerpo del while

print('\nFin.....')
print('Hecho....')
print('--'*30)

#CICLO FOR
print('--'*30)
print('Mostramos todos los valores pertenecientes a un rango....Ciclo For')
for i in range (0,10):
    print(i,' ',end='')                #cuerpo del ciclo

print('Fin del cuerpo')
print('Hecho')
print('--'*30)

#CICLOS EN PASOS DE DOS
#Ahora el bucle se realiza de 0 a 10 pero en pasos de 2
print('Muestra los valores de i de 2 en 2')
for i in range(0, 10, 2):
    print(i,' ', end='')
print()
print()
print('Listo')
print('--'*30)

#UTILIZACIÓN DE COMODÍN
#Usando un comodín 'anónimo'
for _ in range(0,10):
    print('comodín...', end='')
print()
print('--'*30)

#UTILIZACIÓN DE BREAK
for i in range(0,10):
    if i==5:
        break
    print('...Valor de i:', i, end='')
print()
print('--'*30)
#continue y else es posible utilizar en ciclos for
print('--'*30)

alimentos = ["manzanas","bananas","peras",'sandias',"uvas"]
#dada la siguiente lista
print("-"*50)
for a in alimentos:
    print(a)
    #print(alimentos)

##########################################################
print("-"*50)
for a in alimentos:
    if a !='queso':
        print("Hay que comprar queso")
        #break
print(alimentos)
print("-"*50)

########################################################

for letra in "holaa":
    print(letra)
print("-"*50)

########################################################

cont = 0
while cont <= 10:
    print(cont, end='')
    cont = cont+1
print()
print("-"*50)

########################################################








