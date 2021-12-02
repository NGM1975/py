from Figura import *

class Círculo(Figura):  

    def __init__(self,nombre,color,radio):
        super().__init__(nombre,color)
        self.__radio = radio  
        self.setPer(radio)
        self.setArea(radio)

    def setRad(self,radio):
        self.__radio = radio

    def getRad(self):
        return self.__radio

    def setPer(self,radio):
        self.__perímetro = float(2*3.14*radio)

    def getPer(self):
        return self.__perímetro

    def setArea(self,radio):
        self.__área = float(3.14*(radio**2))

    def getArea(self):
        return self.__área

    def mostrarFigura(self):
#        print('CÍRCULO')
        super().mostrarFigura()
        print('RADIO: ',self.getRad())    
        print('PERÍMETRO: ',self.getPer())
        print('ÁREA: ',self.getArea())
        
