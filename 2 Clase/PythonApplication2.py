
mistring = "hOLAmuNdo"
mistring1 = "Pepe"
print(mistring)
#mistring = 1234
#print (mistring)
#Ejemplos

#PARA SABER EL TIPO DE DATO
#print(type(mistring))

#PARA VER UN TEXTO ENTRE COMILLAS
#print('Alguien dijo " Hola a todos!!"...pero no sabemos quien fue')

#PASAJE DE MAYÚSCULAS A MINÚSCULAS Y VICEVERSA
#print("Hola".upper())
#print(mistring. lower())

#INVERTIR MAYÚSCULAS A MINÚSCULAS Y VICEVERSA
#print(mistring.swapcase())
#print(mistring.swapcase())

#CONCATENACIÓN
#mistring2 = mistring + ','+ mistring1
#print(mistring2)
#mistring = "Cadena 1 "+ "Cadena 2"
#print(mistring)

#LONGITUD DE CADENAS
#print("La longitud de mistring es :" + str(len(mistring)))

#ACCESO A CADA CARACTER COMIENZA EN CERO TAMBIEN SE PUEDE ACCEDER A SUBCADENAS
#print(mistring[3])
#print(mistring[0])
#print(mistring[0:6])

#REPETICIÓN DE CADENAS
#print('-+' * 30)
#print(mistring * 10)
#print("PEDRO" * 100)
#print('-*' * 30)

#DIVISIÓN DE CADENAS  función split()
#mistring = "Hola ciudad de Mar del Plata"
#print(mistring.split(' '))
#mistring2 = "Hola, ciudad de, Mar del Plata"
#print(mistring2.split('a'))

#CONTAR SUBCADENAS CONTENIDAS EN OTRA  fución count()
#mistring = "Hola ciudad de Mar del Plata"
#print(mistring.count(' ')) #devuelve la cantidad de espacios en blaco existentes en mistring
#print(mistring.count('de'))

#REEMPLAZAR UNA SUBCADENA EN UNA CADENA   función replace()
#saludo = "Hola xxxx cómo estás?"
#print(saludo.replace("xxxx","María"))    #muestra "Hola María cómo estás?

#SI UNA CADENA ES SUBCADENA DE OTRA    función find()
#saludo = "Hola María cómo estás?"
#print(saludo.find("xxxx"))   #devuelve -1 porque no existe
#print(saludo.find("María"))  #devuelve 5 que es donde comienza

#CONVERSIÓN DE TIPOS   función de str()
#saludo = "Hola María ... tuedad es " + 21   #devuelve error
#saludo = "Hola María ... tu edad es" + str(21)
#print(saludo)

#COMPARACIÓN DE CADENAS  operadores == o !=
#print("Juan" == "Juan")   # muestra True
#print("Juan" == "Juan José")  #muestra False

#UBICACIÓN DE UN CARACTER DENTRO DE UNA CADENA   #función index()
#print(mistring.index('L'))   #devuelve el primer lugar donde se encuentra, sino es ERROR

#SI UNA VARIABLE ES O NO NUMÉRICA   #función isnumeric() e isalpha()
#print(mistring.isnumeric())   #devuelve False
#print(mistring.isalpha())    #devuelvew True si todo su contenido son letras
#mistring = "1234"
#print(mistring.isnumeric())   #devuelve True
#print(mistring.isalpha())   #devuelve False

#SI UNA CADENA ES ALFANUMERICA     #función isalnum()
#cad = 'a1234abCd'
#print(cad.isalnum())

#SECUENCIAS DE ESCAPE IDEM C
#print('hola \n\tcómo va?')

#LOSSUBINDICES DE LAS CADENAS SON IGUALES A C EXEPTO QUE:
#las referencias -1 -2 -3 son los caracteres de final de la cadena
#cad[-1] es la última letra cad [-2] la anteúltima y así...
#mistring1 = "Hola cómo Está?"
#print(mistring1[-1])  #muestra ?
#print(mistring1[-2])  #muestra s

#MUESTRA TODOS LOS ATRIBUTOS MÉTODOS DISPONIBLES DE LA CLASE STRING
#print(dir(mistring))

