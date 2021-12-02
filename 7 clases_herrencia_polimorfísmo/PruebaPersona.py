from Persona import *
#Utilizamos métodos getters y setters, atributos y
#métodos encapsulados
#instanciación de objetos de la clase persona

print('-'*50)
p1 = Persona(30,70,1.80,'Eduardo')
#print('Nombre de la persona : ',p._nombre)  ...error  __nombre es privado
#print(p1._estado()) ...error no se puede acceder a un método
#encapsulado desde fuera del objeto

print('Nombre de la persona: ',p1.getNombre())
p1.muestra()
p1.caminar()
p1.setAltura(1.95)
p1.muestra()

print('-'*50)
p2 = Persona(25,50,1.60,'Anabella')
p2.muestra()
p2.setNombre('María')
p2.setAltura(1.65)
p2.muestra()
print('-'*50)

#---------------------Menu--------------------------
print('---------------------------------------------')


