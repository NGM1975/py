from Usuario import *

class Particular(Usuario):  

    def __init__(self,nombre,dirección,abono,pulsos,DNI,fNac):
        super().__init__(nombre,dirección)
        importe = 1
        self.__DNI = DNI
        self.__fNac = fNac
        self.__abono = abono
        self.setImp(importe,pulsos)


    def setDNI(self,DNI):
        self.__DNI = DNI

    def getDNI(self):
        return self.__DNI

    def setfNac(self,fNac):
        self.__fNac = fNac

    def getfNac(self):
        return self.__fNac

    def getImp(self):
        return self.__importe

    def setImp(self,importe,pulsos):
       
        if pulsos>1000:           
                importe = float(pulsos*1.2)
        elif pulsos>=401 and pulsos<=1000 :
                importe = float(pulsos*1.0)
        elif pulsos>=201 and pulsos<=400 :
                importe = float(pulsos*0.7)
        elif pulsos>=0 and pulsos<=200 :
                importe = float(pulsos*0.5)
        self.__importe = importe

    def setAb(self,abono):
        self.__abono = abono

    def getAb(self):
        return self.__abono

    def mostrarUsuario(self):  
        print('PARTICULAR')
        super().mostrarUsuario()  
        print('DNI: ',self.getDNI())
        print('FECHA DE NACIMIENTO(año/mes/día): ',self.getfNac())
        print('ABONO: $',self.getAb())
        print('IMPORTE: $',self.getImp())
        print('TOTAL A PAGAR: $',self.getImp()+300)
        