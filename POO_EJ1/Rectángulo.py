from Figura import *

class Rectángulo(Figura):  

    def __init__(self,nombre,color,lado1,lado2):
        super().__init__(nombre,color)
        self.__lado1 = lado1
        self.__lado2 = lado2  
        self.setPer(lado1,lado2)
        self.setArea(lado1,lado2)

    def setLado1(self,lado1):
        self.__lado1 = lado1

    def getLado1(self):
        return self.__lado1

    def setLado2(self,lado2):
        self.__lado2 = lado2

    def getLado2(self):
        return self.__lado2

    def setPer(self,lado1,lado2):
        self.__perímetro = float((lado1*2)+(lado2*2))

    def getPer(self):
        return self.__perímetro

    def setArea(self,lado1,lado2):
        self.__área = float(lado1*lado2)

    def getArea(self):
        return self.__área    

    def mostrarFigura(self):
#        print('RECTÁNGULO')        
        super().mostrarFigura()
        print('LADO 1: ',self.getLado1())
        print('LADO 2: ',self.getLado2())    
        print('PERÍMETRO: ',self.getPer())
        print('ÁREA: ',self.getArea())
        