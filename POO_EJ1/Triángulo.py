from Figura import *

class Triángulo(Figura):  

    def __init__(self,nombre,color,base,altura,l2,l3):
        super().__init__(nombre,color)  
        self.__base = base
        self.__altura = altura
        self.setPer(base,l2,l3)
        self.setArea(base,altura)

    def setBase(self,base):
        self.__base = base

    def getBase(self):
        return self.__base

    def setAltura(self,altura):
        self.__altura = altura

    def getAltura(self):
        return self.__altura

#    def setLado2(self,l2):
#        self.__lado2 = l2

#    def getLado2(self):
#        return self.__lado2

#    def setLado3(self,l3):
#        self.__lado3 = l3

#    def getLado3(self):
#        return self.__lado3

    def setPer(self,base,l2,l3):
        self.__perímetro = float(base+l2+l3)

    def getPer(self):
        return self.__perímetro

    def setArea(self,base,altura):
        self.__área = float((base*altura)/2)

    def getArea(self):
        return self.__área

    def mostrarFigura(self):
#        print('TRIÁNGULO')
        super().mostrarFigura()
        print('BASE: ',self.getBase())
        print('ALTURA: ',self.getAltura())
        print('PERÍMETRO: ',self.getPer())
        print('ÁREA: ',self.getArea())
        