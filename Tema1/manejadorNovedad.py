import csv
from novedad import Novedad
class manejadorN:
    __listaN: list
    
    def __init__(self):
        self.__listaN = []
    
    def cargarListaN(self):
        archivo= open("novedades.csv")
        reader= csv.reader(archivo, delimiter=";")
        next (reader)
        for fila in reader:
            unaNovedad = Novedad(fila[0], int(fila[1]), fila[2], fila[3])
            self.__listaN.append(unaNovedad)
        archivo.close()
    
    def mostrarListaN(self):
        for i in range (len(self.__listaN)):
            print("Legajo: {}, Importe: {}, Concepto: {}, Codigo: {}".format(self.__listaN[i].getLeg(), self.__listaN[i].getImporte(), self.__listaN[i].getConcepto(), self.__listaN[i].getCod()))
    
    
    def ObtenerDescuento(self, legajo):
        des= 0
        for i in range(len(self.__listaN)):
            if self.__listaN[i].getLeg() == legajo:
                if self.__listaN[i].getCod() == "D":
                    des += self.__listaN[i].getImporte()
        
        return des
    
    def ObtenerAumento(self, legajo):
        aum=0
        for i in range(len(self.__listaN)):
            if self.__listaN[i].getLeg() == legajo:
                if self.__listaN[i].getCod() == "A":
                    aum += self.__listaN[i].getImporte()
        return aum
    
    def mostrar(self, leg):
        for i in range(len(self.__listaN)):
            if self.__listaN[i].getLeg() == leg:
                print("Codigo: {} \t Concepto: {} \t \t Importe:{}".format(self.__listaN[i].getCod(), self.__listaN[i].getConcepto(), self.__listaN[i].getImporte()))