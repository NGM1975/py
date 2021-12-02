examenes = {'Andrés', 'Katy', 'Bety', 'Emilio', 'Susana'}
proyectos = {'Katy', 'Emilio', 'Iván', 'Eduardo'}
print('Exámenes:', examenes)
print('Proyectos:', proyectos) 
print('*'*50)
#1a)
print(examenes & proyectos)  #{'Katy', 'Emilio'}
#1b)
print(examenes - proyectos)  #{'Andrés','Bety','Susana'}
#1c)
print(proyectos - examenes)  #{'Iván','Eduardo'}
#1d)
print(list(examenes | proyectos))  #['Eduardo','Emilio','Susana','Andrés','Iván','Katy','Bety']
#1e)
print(list(examenes ^ proyectos)) #['Eduardo','Bety','Susana','Iván','Andrés']
print()
print('-'*50)
#2)
print()
#a)
frase = input("Ingrese frase...: \n\t")
#b)
frase = (frase.split())
print(frase)
print()
print('*'*50)
#c) 
print()
from collections import Counter   # no me tomaba el counter si no hacía esto
contador = Counter(frase)
print(contador)
print()
print('+'*50)
#d)#e)
print()
lista =  sorted(contador.items())
print(lista)
print()
print('+'*50)

