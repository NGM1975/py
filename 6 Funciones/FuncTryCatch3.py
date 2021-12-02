#------------------------------------------------------

def dividir3():
    try:
        op1 = float(input("Ingrese primer Número: "))
        op2 = float(input('Ingrese segundo Número: '))
        print("Resultaso de la didvisión3 es...: " + str(op1/op2))

    except ValueError:
        print("Error en el tipo de datos ingresados...")    
    except ZeroDivisionError:
        print("No se puede dividir por cero...")
    except IOError:
        print("No se puedo abrir el archivo...")
    finally: #esto se ejecuta en caso que no haya existido errores
        print("Fin de la operación...")
    
while True:
    dividir3()
    