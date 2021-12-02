from Usuario import *

class Profesional(Usuario):  

    def __init__(self,nombre,dirección,abono,pulsos,área,título):
        super().__init__(nombre,dirección)
        importe = 1
        self.__área = área
        self.__título = título
        self.__abono = abono
        self.setImp(importe,pulsos)

    def setArea(self,área):
        self.__área = área

    def getArea(self):
        return self.__área

    def setfTit(self,título):
        self.__título = título

    def getfTit(self):
        return self.__título

    def getImp(self):
        return self.__importe

    def setImp(self,importe,pulsos):
       
        if pulsos>1000:           
                importe = float(pulsos*1.5)
        elif pulsos>=401 and pulsos<=1000 :
                importe = float(pulsos*1.3)
        elif pulsos>=201 and pulsos<=400 :
                importe = float(pulsos*1.1)
        elif pulsos>=0 and pulsos<=200 :
                importe = float(pulsos*0.7)
        self.__importe = importe

    def setAb(self,abono):
        self.__abono = abono

    def getAb(self):
        return self.__abono

    def mostrarUsuario(self):  
        print('PROFESIONAL')
        super().mostrarUsuario()  
        print('ÁREA: ',self.getArea())
        print('TÍTULO: ',self.getfTit())
        print('ABONO: $',self.getAb())
        print('IMPORTE: $',self.getImp())
        print('TOTAL A PAGAR: ',self.getImp()+500,'$')