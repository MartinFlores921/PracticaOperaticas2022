class Novedad:
    __leg = ""
    __importe = 1
    __concepto = ""
    __codigo = ""
    
    def __init__(self, le, imp, con, cod):
        self.__leg = le
        self.__importe = imp
        self.__concepto= con
        self.__codigo = cod
    
    def getLeg(self):
        return self.__leg
    def getImporte(self):
        return self.__importe
    def getConcepto(self):
        return self.__concepto
    def getCod(self):
        return self.__codigo
  