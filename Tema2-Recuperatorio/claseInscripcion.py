class Inscripcion:
    __id= ""
    __apellido= ""
    __nombre= ""
    __dni= ""
    __prov=""
    __estado= ""
    def __init__(self,id,ape,nom,dni,provin,est):
        self.__id= id
        self.__apellido= ape
        self.__nombre= nom
        self.__dni= dni
        self.__prov= provin
        self.__estado= est
  
    
    def getId(self):
        return self.__id
    
    def getApellido(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre
    def getDni(self):
        return self.__dni
    def getProv(self):
        return self.__prov
    def getEstado(self):
        return self.__estado
    
    def __eq__(self, otro):
        if isinstance(otro, Inscripcion):
            a= self.__apellido + self.__nombre + self.__dni + self.__prov
            b= otro.__apellido + otro.__nombre + otro.__dni + otro.__prov
            return a == b
    def setEstado(self):
        self.__estado = "R"
        return self.__estado
    def setEstadoA(self):
        self.__estado = "A"
        return self.__estado
    def __lt__(self, otro):
        if isinstance(otro,Inscripcion):
            a= self.__apellido 
            b= otro.__apellido
            return a < b 
        