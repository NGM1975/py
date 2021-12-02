class Figura():
    def __init__(self,nombre,color):
        self.__nombre = nombre
        self.__color = color
        self.mueve = True

    def setNom(self,nombre):
        self.__nombre = nombre

    def getNom(self):
        return self.__nombre

    def setColor(self,color):
        self.__color = color

    def getColor(self):
        return self.__color

    def mover(self):
        self.mueve = True

###############################################################
    def mostrarFigura(self):
        print('NOMBRE: ',self.getNom())
        print('COLOR: ',self.getColor())
        dy = (float(input('Ingrese valor de movimiento en eje y: ')))
        dx = (float(input('Ingrese valor de movimiento en eje x: ')))
        if dy == 0 and dx == 0:
                print('La figura no se mueve')
                self.mueve = False
        if self.mueve:
            print('Figura en movimiento')
            if dy!= 0:
                if dy<0:
                    if dx<0:
                        print('La figura desciende ',dy,'cm y retrocede',dx,'cm')
                    elif dx>0:
                        print('La figura desciende ',dy,'cm y avanza',dx,'cm')
                    else:
                        print('La figura solo desciende ',dy,'cm')
                elif dy>0:
                    if dx<0:
                        print('La figura sube ',dy,'cm y retrocede',dx,'cm')
                    elif dx>0:
                        print('La figura sube ',dy,'cm y avanza',dx,'cm')
                    else:
                        print('La figura solo sube ',dy,'cm')
            elif dy == 0:
                if dx<0:
                    print('La figura solo retrocede',dx,'cm')
                elif dx>0:
                    print('La figura solo avanza',dx,'cm')

 #########################################################################################


                
                
