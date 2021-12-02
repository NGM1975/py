from Usuario import *

class Comercial(Usuario):  

    def __init__(self,nombre,dirección,abono,pulsos,rubro,cuit):
        super().__init__(nombre,dirección)
        importe = 1
        self.__rubro = rubro
        self.__cuit = cuit
        self.__abono = abono
        self.setImp(importe,pulsos)

    def setRub(self,rubro):
        self.__rubro = rubro

    def getRub(self):
        return self.__rubro

    def setfCuit(self,cuit):
        self.__cuit = cuit

    def getCuit(self):
        return self.__cuit

    def getImp(self):
        return self.__importe

    def setImp(self,importe,pulsos):
       
        if pulsos>1000:           
                importe = float(pulsos*1.7)
        elif pulsos>=401 and pulsos<=1000 :
                importe = float(pulsos*1.5)
        elif pulsos>=201 and pulsos<=400 :
                importe = float(pulsos*1.2)
        elif pulsos>=0 and pulsos<=200 :
                importe = float(pulsos*0.9)
        self.__importe = importe

    def setAb(self,abono):
        self.__abono = abono

    def getAb(self):
        return self.__abono

    def mostrarUsuario(self):  
        print('COMERCIAL')
        super().mostrarUsuario()  
        print('RUBRO: ',self.getRub())
        print('CUIT: ',self.getCuit())
        print('ABONO: $',self.getAb())
        print('IMPORTE: $',self.getImp())
        print('TOTAL A PAGAR: ',self.getImp()+700,'$')