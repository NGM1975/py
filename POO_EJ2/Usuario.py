class Usuario():
    def __init__(self,nombre,dirección):
#        importe = 1
        self.__nombre = nombre
        self.__dirección = dirección 
#        self.__abono = abono
#        self.__pulsos = pulsos
#        self.setImp(importe,pulsos)   
        self.baja = False
        
#    def getImp(self):
#        return self.__importe

#    def setImp(self,importe,pulsos,abono):
#        
#        if pulsos>1000:
#            if abono== 1:
#                importe = float(pulsos*1.2)
#            elif abono == 2:
#                importe = float(pulsos*1.5)
#            elif abono ==3:
#                importe = float(pulsos*1.7)
#        elif pulsos>=401 and pulsos<=1000 :
#            if abono == 1:
#                importe = float(pulsos*1.0)
#            elif abono == 2:
#                importe = float(pulsos*1.3)
#            elif abono ==3:
#                importe = float(pulsos*1.5)
#        elif pulsos>=201 and pulsos<=400 :
#            if abono == 1:
#                importe = float(pulsos*0.7)
#            elif abono == 2:
#                importe = float(pulsos*1.1)
#            elif abono ==3:
#                importe = float(pulsos*1.2)
#        elif pulsos>=0 and pulsos<=200 :
#            if abono == 1:
#                importe = float(pulsos*0.5)
#            elif abono == 2:
#                importe = float(pulsos*0.7)
#            elif abono ==3:
#                importe = float(pulsos*0.9)
#        self.__importe = importe
   

    def setNom(self,nombre):
        self.__nombre = nombre

    def getNom(self):
        return self.__nombre

    def setDirec(self,dirección):
        self.__dirección = dirección

    def getDirec(self):
        return self.__dirección

#    def setPul(self,pulsos):
#        self.__pulsos = pulsos

#    def getPul(self):
#        return self.__pulsos

#    def setAb(self,abono):
#        self.__abono = abono

#    def getAb(self):
#        return self.__abono

    def darBaja(self):
        self.baja = True

    def darAlta(self):
        self.baja = False

    def mostrarUsuario(self):
        print('NOMBRE: ',self.getNom())
        print('DIRECCIÓN: ',self.getDirec())
#       if self.getAb() == 1:
#            print('ABONO: $300')
#        elif self.getAb() == 2:
#            print('ABONO: $500')
#        elif self.getAb() == 3:
#            print('ABONO: $700')

        if self.baja:
            print('Servicio dado de baja')
        else:
            print('Servicio activo')
#            print('IMPORTE: ',self.getImp(),'$')    


