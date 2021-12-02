# Primer ejemplo de funciones

def sumar():
    n1 =  int(input('ingrese primer número a sumar...'))
    n2 = input('ingrese segundo número a sumar...')
#    print('La suma de  ',n1, 'más ',n2, 'es', n1+n2)
    #esto concatena n1 y n2
    print('La suma de',n1, 'más',n2, 'es', n1 + int(n2))
    #esto realiza la suma algebraica

print('*'*50)
sumar()
print('*'*50)
#------------------------------------------------------------
#Segundo ejemplo de funciones con parámetros

def multiplicar(p1,p2):  #parámetros separados por comas
    print('Resultado de multiplicar es: ',p1*p2)

print('*'*50)
multiplicar(10,3) #parámetros literales
#respetar cantidad y orden de los parámetros
a1 = float(input('Ingrese primer número para multiplicar: '))
a2 = int(input('Ingrese segundo número para multiplicar: '))

print('*'*50)
multiplicar(a1,a2)
print('*'*50)
#------------------------------------------------------------


