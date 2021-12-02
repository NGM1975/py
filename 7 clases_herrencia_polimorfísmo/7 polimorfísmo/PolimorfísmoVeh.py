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

########################################################
class Camioneta(Vehículo):  #herencia simple

    def __init__(self,marca,modelo,año,ruedas,peso):
        super().__init__(marca,modelo,año,ruedas)  #reutilización contructor
        self.peso = peso

    def cargar(self,peso):
        self.peso = peso
        if self.peso:
            return "La camioneta está cargada con ",self.peso ,"Kg"
        else:
            return "La camioneta está vacía..."

    def mostrarVehículo(self):  #sobreescritura del método muestra del padre
        super().mostrarVehículo()  #reutilización de muestra vehículo
        print('CARGA: ',self.peso)

##########################################################
class Moto(Vehículo):   #herencia

    def __init__(self,marca,modelo,año,ruedas):
        super().__init__(marca,modelo,año,ruedas)  #reutilización contructor
        self.willy = ""

    def hacerWilly(self): #Método propio de la clase moto
        self.willy = "El vehículo está haciendo Willy"

    def mostrarVehículo(self):  #sobreescritura del método muestra del padre
        super().mostrarVehículo()  #reutilización de muestra vehículo
        print(self.willy)

###########################################################
class Cuatriciclo(Moto):   #HERENCIA EN CASCADA (de Vehículo y Moto)
    def __init__(self,marca,modelo,año,ruedas,cilindrada):
        super().__init__(marca,modelo,año,ruedas)  #reutilización contructor
        self.cilindrada = cilindrada
        self.willy = ""

    def setCil(self,cilindrada):
        self.cilindrada = cilindrada

    def getCil(self):
        return self.cilindrada

    def mostrarVehículo(self):  #sobreescritura del método muestra del padre
        super().mostrarVehículo()  #reutilización de muestra vehículo
        print('CILINDRADA: ',self.cilindrada)
        print(self.willy)

##############################################################
class Veléctricos():    #NO HEREDA DE NADIE
    autonomía = 1
    def __init__(self):
        self.autonomía = 100

    def setAutonomía(self,autonomía):
        self.autonomía = autonomía
        
    def getAutonomía(self):
        return self.autonomía

    def cargaBatería(self):
        self.cargado = True

#####################################################################
class Bicieléctrica(Vehículo,Veléctricos):  #Herencia múltiple hereda de dos clases distintas

    def __init__(self,marca,modelo,año,ruedas,autonomía,rodado):
        super().__init__(marca,modelo,año,ruedas)   #constructor de Vehículos
        self.rodado = rodado
        self.autonomía = autonomía

    def setRodado(self,rodado):
        self.rodado = rodado

    def getRodado(self):
        return self.rodado

    def mostrarVehículo(self):  #sobreescritura del método muestra del padre
        super().mostrarVehículo()  #reutilización de muestra vehículo
        print('RODADO: ',self.rodado)
        print('AUTONOMÍA: ',self.getAutonomía())

#######################################################################
    
