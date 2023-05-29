import csv
from  claseCurso import Curso
class manejadorC:
    __listaC: list
    
    def __init__(self):
        self.__listaC= []
    
    def cargarListaC(self):
        archivo= open("cursos.csv")
        reader= csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            unCurso= Curso(fila[0], fila[1], int(fila[2]), fila[3], int(fila[4]), int(fila[5]))
            self.__listaC.append(unCurso)
        archivo.close()
    
    def mostrarListaC(self):
        for i in range(len(self.__listaC)):
            print("IdCurso: {}, Denominacion: {}, CantHs: {}, Provincia: {}, CupoIns: {}, CupoAcep: {}".format(self.__listaC[i].getIdCurso(), self.__listaC[i].getDenominacion(), self.__listaC[i].getCantHs(), self.__listaC[i].getProvincia(), self.__listaC[i].getCupoIns(), self.__listaC[i].getCupoAcep()))
    def ObtenerCupo(self, id):
        for i in range(len(self.__listaC)):
            if self.__listaC[i].getIdCurso() == id:
                cupo= self.__listaC[i].getCupoIns()
        
        return cupo
    def Listar(self, id):
        for i in range(len(self.__listaC)):
            if self.__listaC[i].getIdCurso() == id:
             print("IdCurso: {} \t CantHs: {}".format(self.__listaC[i].getIdCurso(), self.__listaC[i].getCantHs()))
             