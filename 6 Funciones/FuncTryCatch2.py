#------------------------------------------------------

def dividir2(op1,op2):
    try:
        return op1/op2
    except ZeroDivisionError:
        print("No se puede dividir por cero...")
        return "Operación inválida"

while True:
    try:
        n1 = int(input("Ingrese primer Número: "))
        n2 = int(input('Ingrese segundo Número: '))
        break
    except ValueError:
        print("Tipos de datos incorrectos....Vuelva a ingresarlos")

print("Resultaso de la didvisión2 es...: ",dividir2(n1,n2))