class Curso:
    __idCurso= ""
    __denominacion= ""
    __cantHs= 0
    __provincia= ""
    __cupoIns= 0
    __cupoAcep= 0
    def __init__(self,id,den,cantH,prov,cupoi,cupoA):
        self.__idCurso= id
        self.__denominacion= den
        self.__cantHs= cantH
        self.__provincia= prov
        self.__cupoIns= cupoi
        self.__cupoAcep= cupoA
        
    def getIdCurso(self):
        return self.__idCurso
    
    def getDenominacion(self):
        return self.__denominacion
    
    def getCantHs(self):
        return self.__cantHs
    def getProvincia(self):
        return self.__provincia
    def getCupoIns(self):
        return self.__cupoIns
    def getCupoAcep(self):
        return self.__cupoAcep
    
        
        