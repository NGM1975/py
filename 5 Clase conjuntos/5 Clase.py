#Operaciones propias de conjuntos
#UNIÓN
print('*'*50)
c1 = {1,2,3}
c2 = {3,4,5,6}
print('unión de c1 con c2 es: ',c1|c2)
print('*'*50)
#---------------------------------------- n
c3 = {'Bananas','Peras','Manzanas'}
c4 = {'Sandias','Peras','Melones'}
c5 = c3|c4
print('Unión de c3 y c4 es: ',c5)
print('*'*50)
#---------------------------------------
#INTERSECCIÓN (pertenecen a ambos...elementos en común)
print('Intersección entre c3 y c4: ',c3 & c4)
print('*'*50)
#---------------------------------------
print('*'*50)
#DIFERENCIA  (todo lo que está en c1 y no en c2)
print('c1 - c2 es: ',c1-c2)
#---------------------------------------
print('*'*50)
#DIFERENCIA SIMÉTRICA  (es el inverso de la intersección ... los q no son comunes a ambos sets)
print('Ladiferencia simétrica entre c1 y c2 es: ',c1^c2)
print('Ladiferencia simétrica entre c3 y c4 es: ',c3^c4)
#------------------------------------------
print('*'*50)
#todos estos operadores de conjunto están disponibles como métodos
