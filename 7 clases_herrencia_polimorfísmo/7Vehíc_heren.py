#clases definiciones
class Vehículo():
    def __init__(self,marca,modelo,año,ruedas):
        self.__marca = marca
        self.__modelo = modelo
        self.__ruedas = ruedas
        self.__año = año
        self.estado = False
        self.acelerar = False
        self.frenar = False

    def setMarca(self,marca):
        self.__marca = marca

    def getMarca(self):
        return self.__marca

    def setModelo(self,modelo):
        self.__modelo = modelo

    def getModelo(self):
        return self.__modelo

    def setRuedas(self,ruedas):
        self.__ruedas = ruedas

    def getRuedas(self):
        return self.__ruedas

    def setAño(self,año):
        self.__año = año

    def getAño(self):
        return self.__año

    def arrancar(self):
        self.estado = True

    def parar(self):
        self.estado = False

    def acelera(self):
        self.frenar = False
        self.acelerar = True

    def frena(self):
        self.frenar = True
        self.acelerar = False

    def mostrarVehículo(self):
        print('MARCA: ',self.getMarca())
        print('MODELO: ',self.getModelo())
        print('AÑO: ',self.getAño())
        print('RUEDAS: ',self.getRuedas())
        if self.estado:
            print('Este vehículo está en marcha')
        else:
            print('Vehículo parado')
        if self.acelerar:
            print('Este vehículo está acelerando')
        else:
            print('El vehículo está frenado')
###################################################################
class Camioneta(Vehículo):   #herencia simple
    def cargar(self,Kg):
        self.peso = Kg
        if self.peso:
            return "La camioneta está cargada con ",self.peso,"Kg"
        else:
            return "La camioneta está vacía..."

####################################################################
class Moto(Vehículo): #herencia simple
    #self __init__(self,marca,modelo,año,ruedas)
    Willy = ""
    def hacerWilly(self):  #Método propio de la clase moto
        self.Willy = "El vehículo está haciendo willy"

    def mostrarVehículo(self):   #Sobreescritura del método muestra del padre
        print('MARCA: ',self.getMarca())
        print('MODELO: ',self.getModelo())
        print('AÑO: ',self.getAño())
        print('RUEDAS: ',self.getRuedas())
        if self.estado:
            print('Este vehículo está en marcha')
        else:
            print('Vehículo parado')
        if self.acelerar:
            print('Este vehículo está acelerando')
        else:
            print('El vehículo está frenado')
        print(self.Willy)

###################################################################
class Cuatriciclo(Moto):   #Herencia en cascada (de vehículo y de moto)
    cilindrada = 0
    def setCil(self,cilindrada):
        self.cilindrada = cilindrada

    def getCil(self):
        return self.cilindrada

    def mostrarVehículo(self):   #Sobreescritura del método muestra del padre
        print('MARCA: ',self.getMarca())
        print('MODELO: ',self.getModelo())
        print('AÑO: ',self.getAño())
        print('RUEDAS: ',self.getRuedas())
        print('CILINDRADA: ',self.getCil())
        if self.estado:
            print('Este vehículo está en marcha')
        else:
            print('Vehículo parado')
        if self.acelerar:
            print('Este vehículo está acelerando')
        else:
            print('El vehículo está frenado')
        print(self.Willy)

####################################################################
class Veléctricos():  #No hereda de  nadie
    #autonomía = 1
    def __init__(self):
        self.autonomía = 100

    def getAutonomía(self):
        return self.autonomía

    def setAutonomía(self,autonomía):
        self.autonomía = autonomía

    def cargaBatería(self):
        self.cargado = True

#####################################################################
class Bicieléctrica(Vehículo,Veléctricos):  #Herencia múltiple hereda de dos clases distintas
    rodado = 28
    def setRodado(self,rodado):
        self.rodado = rodado

    def getRodado(self):
        return self.rodado
          
#Siempre hereda el constructor de la primera clase nombrada

######################################################################
print('*'*70)
M = Moto('Yamaha',"Teneré",2017,2)
M.acelera()
M.hacerWilly()
M.mostrarVehículo()
print('*'*70)
miCuatri = Cuatriciclo('Honda','Modelo III',2018,4)   #constructor de class Vehículo
miCuatri.setCil(350)   #Método propio de class Cuatriciclo
miCuatri.acelera()     #Método heredado de class Vehículo
miCuatri.hacerWilly()  #Método heredado de class Moto
miCuatri.mostrarVehículo()
print('*'*70)
#######################################################################
print('#'*70)
MiBici = Bicieléctrica('Curuchet','M450',2020,2)   #Constructor heredado de la clase Vehículo
MiBici.setMarca('Shimano')  #Método herredado de Vehículo
MiBici.cargaBatería()   #Método heredado de veléctricos
MiBici.setRodado(26)    #Método propio de la clase
MiBici.mostrarVehículo()  #Ver como mostrar bien... Faltan atributos
MiBici.setAutonomía(50)
print('Autonomía de la Bici: ',MiBici.getAutonomía())
print('#'*70)

######################################################################
