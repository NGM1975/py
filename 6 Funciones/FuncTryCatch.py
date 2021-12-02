#from Funciones import dividir

def dividir(op1,op2):
    try:
        return op1/op2
    except:
#        print("No se puede dividir por cero...")
        return "Operación inválida"

n1 = int(input("Ingrese primer Número: "))
n2 = int(input('Ingrese segundo Número: '))
print('Resultado de la división: ',dividir(n1,n2))

#------------------------------------------------------

def dividir1(op1,op2):
    try:
        return op1/op2
    except ZeroDivisionError:
        print("No se puede dividir por cero...")
        return "Operación inválida"

n3 = int(input("Ingrese primer Número: "))
n4 = int(input('Ingrese segundo Número: '))
print("Resultaso de la didvisión1 es...: ",dividir1(n3,n4))
