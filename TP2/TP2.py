Nombre = 'nicolás'
Apellido = "garcía"
Apellido2 = 'marín'

#2)
 
print(Nombre + Apellido + Apellido2)
Nombyapell = Nombre +' '+ Apellido +' '+ Apellido2
print(Nombyapell)

print(Nombyapell.replace(" ","*"))   # 1) Espacios x asteríscos

print("La longitud de 'Nombyapell' es :" + str(len(Nombyapell)))

print(Nombyapell. upper())
print(Nombyapell. lower())

print(Nombyapell.find("Fernández"))  

print(Nombyapell[0].upper())
print(Nombyapell[8].upper())
print(Nombyapell[-5].upper())
print(Nombyapell.replace("nicolás garcía marín","Nicolás García Marín"))

print(Nombyapell)
print(Nombyapell.title())

#3)

aux = 'r'
Nombre1 = 'roberto'
print(Nombre1)
print(aux)
print(Nombre1.find(aux))
print(Nombre1.index(aux))
print(Nombre1.count(aux))

#4)

cadena = "Este anyo estaremos mejor"
print(cadena)
print(cadena.replace('ny','ñ'))

#5)hola caracola

frase = "alocarac aloh"
frase_invertida = ''.join(reversed(frase))
inversa_frase = frase[::-1]
print()
print(frase)
print(frase_invertida)
print(inversa_frase)
#for a in frase:
    #print(frase[-1])
    