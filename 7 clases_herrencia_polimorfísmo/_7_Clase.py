class Persona():
#atributos
    edad = 20
    peso = 60
    altura = 1.75
    nombre = "Daniel"
    camina = False
    lee = True

#-----------------------------------------
#métodos
    def caminar(self):
        #print('La persona cambia de posición')
        self.camina = True

    def parar(self):
        #print('La persona no cambia de posición')
        self.camina = False

    def leer(self):
        self.lee = True

    def noleer(self):
        self.lee = False

#------------------------------------------

    def estado(self):
        if(self.camina == True):
            if self.lee:
                return 'está caminando y leyendo'
            else:
                return 'está caminando y sin leer'
        else:
            if self.lee:
                return 'está parada y leyendo...'
            else:
                return 'esta parada y sin leer...'

#--------Instanciación de objetos-------------
#------Ejecución/invocación  de métodos-------

print('-'*50)
p = Persona()
print('Nombre de la persona: ',p.nombre)
print('Altura de la persona: ',p.altura, 'metros')
p.leer()
p.caminar()
print('-'*50)
print('La persona de nombre : ',p.nombre, 'está ', p.estado())
print('-'*50)
p.parar()
#p.noleer()
print('La persona de nombre: ',p.nombre, 'está ', p.estado())
print('-'*50)
#------Más objetos de la misma clase---------
p1 = Persona()
print('La persona de nombre: ',p1.nombre, 'está ', p1.estado())
#--------------------------------------------



