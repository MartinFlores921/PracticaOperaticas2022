class Personal:
    __legajo = ""
    __dni = ""
    __apellido = ""
    __nombre = ""
    __sueldoBasico = 1
    __sueldoTotal= 0
    def __init__(self, leg, dni, ape, nom, sueldoB, sueldoT=0):
        self.__legajo = leg
        self.__dni = dni
        self.__apellido= ape
        self.__nombre = nom
        self.__sueldoBasico = sueldoB
        self.__sueldoTotal = sueldoT
    
    def getLegajo(self):
        return self.__legajo
    def getDni(self):
        return self.__dni
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getSueldoBasico(self):
        return self.__sueldoBasico
    def getAyN(self):
        return self.__apellido + " " + self.getNombre
    def getSueldoTotal(self):
        return self.__sueldoTotal
    
    def ActualizarSueldo(self, des, aum):
        self.__sueldoTotal= self.__sueldoBasico + aum - des
    
    def __lt__(self, otro):
        if isinstance(otro,Personal):
          return self.__sueldoTotal < otro.__sueldoTotal
        #else:
            #return self.__sueldoTotal < otro
    #self.__apellido + " " + self.__nombre
    def __gt__(self, otro):
        if isinstance(otro,Personal):
            return self.getApellido() > otro.getApellido()
        
