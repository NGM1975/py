
def armarListaPares(tope):
    num = 0
    lista = []
    while num < tope:
        lista.append(num * 2)
        num = num +1
    return lista

#-----------------------------------------------------------------
print('-'*50)
límite = input('Ingrese el límite superior de la lista: ')
print('Lista generada es: ', armarListaPares(int(límite)))
print('-'*50)
#-----------------------------------------------------------------
#-----------------------------------------------------------------
#Utilizando generadores o funciones yield
def armarListaParesYield(tope):
    num = 0
    while num < tope:
        yield num * 2
        num = num + 1

#------------------------------------------------------------------
print('-'*50)
pares = armarListaParesYield(int(límite))
#para mostrar
#for i in pares:
#    print('[',i,']', end= '')

print('\n')
#------------------------------------------------------------------
print('-'*50)
#distintas invocaciones para ver que queda en suspenso
print("Al mostrar de a uno....\n")
print(next(pares))
print('Siguiente número...')
print(next(pares))
print('Siguiente número...')
print(next(pares))
print('Siguiente número...')
print(next(pares))
print('Siguiente número...')
print(next(pares))
print('Siguiente número...')
print(next(pares))