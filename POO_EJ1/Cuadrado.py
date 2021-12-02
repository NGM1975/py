from Figura import *

class Cuadrado(Figura):  

    def __init__(self,nombre,color,lado):
        super().__init__(nombre,color)
        self.__lado = lado  
        self.setPer(lado)
        self.setArea(lado)

    def setLado(self,lado):
        self.__base = lado

    def getLado(self):
        return self.__lado

    def setPer(self,lado):
        self.__perímetro = float(lado*4)

    def getPer(self):
        return self.__perímetro

    def setArea(self,lado):
        self.__área = float(lado**2)

    def getArea(self):
        return self.__área

    def mostrarFigura(self):
#        print('CUADRADO')     
        super().mostrarFigura()
        print('LADO: ',self.getLado())
        print('PERÍMETRO: ',self.getPer())
        print('ÁREA: ',self.getArea())
        