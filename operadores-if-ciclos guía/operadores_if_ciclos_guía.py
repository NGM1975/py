#1)
km = (int(input('Escriba la cantidad de km...: ')))
milla = km/0.6214
print("El valor en milla de los km ingresados es...: ",milla)

#2)
km =(int(input('Escriba la cantidad de km...: ')))
while km<0:
    print(km," es un valor negativo\n")
    km = (int(input('Escriba la cantidad de km...: ')))
milla = km/0,6214
print("El valor en milla de los km ingresados es...: ",milla)

#3)
lista = int(input('¿Hasta qué número quieres la lista?: '))
cont = 0
for i in range(2, lista + 1):
   primos = True
    for j in range(2,11):
        if i == j:
           break
        elif i%j == 0:
           primos = False
        else:
           continue
    if primos == True:
        print(' ',i, end='')
        cont += 1
print('\nHay %u números primos.' % cont )
print("++"*50)

número =(int(input('Escriba un número...: ')))
while número<2:
    print(número,"Error: valor ingresado < 2\n")
    número = int(input('Escriba un número...: '))
for a in range(2,número+1):
    primos = True
    for j in range(2,a):
        if a%j == 0:
            primos = False
    if primos == True:
        print(' ',a, end='')
print("\n")
print("++"*50)

#4)
d = 3
b = 11
for x in range(d,b+1):
    print(' ',x, end='')
print("\n")
for y in range(b,d-1, -1):
   print(' ',y, end='')
print("\n")

print("++"*50)

#5)
for x in range(0,8):
    print()
    for y in range (0,8):
        if x != y:
            if (x%2 == 0 and y%2 != 0) or (x%2 != 0 and y%2 == 0):
                print('B','  ', end='')
                
            else:
                print("N",'  ',end='')
        else:
            print('0','  ',end='')

print("\n")

print("++"*50)
            
        
            
        
            

        
        
            


            
            

        

    