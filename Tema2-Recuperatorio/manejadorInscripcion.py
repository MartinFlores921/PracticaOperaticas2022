import csv
from claseInscripcion import Inscripcion
class manejadorI:
    __listaI: list
    
    def __init__(self):
        self.__listaI= []
    
    def cargarListaI(self):
        archivo= open("inscripciones.csv")
        reader= csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            unaInstancia= Inscripcion(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
            self.__listaI.append(unaInstancia)
        archivo.close()
    
    def mostrarListaI(self):
        for i in range(len(self.__listaI)):
            print("Id:{}, Apellido: {}, Nombre:{}, Dni: {}, Prov: {}, Estado: {}".format(self.__listaI[i].getId(), self.__listaI[i].getApellido(), self.__listaI[i].getNombre(), self.__listaI[i].getDni(), self.__listaI[i].getProv(),self.__listaI[i].getEstado()))
    
    def inciso1(self, dni):
        i=0
        c=0
        for i in range (len(self.__listaI)):
            if self.__listaI[i].getDni() == dni:
                c+=1
                a= self.__listaI[i]
                if a == self.__listaI[i]:
                     if c>1:
                          self.__listaI[i].setEstado()
        #for i in range(len(self.__listaI)):
            """if a == self.__listaI[i]:
                if c>1:
                 self.__listaI[i].setEstado()"""
    
    def inciso2(self, id, curso):
        cup=0
        c=0
        for i in range(len(self.__listaI)):
            if self.__listaI[i].getId() == id:
                cup= curso.ObtenerCupo(id)
                c+=1
            if c < cup :
             self.__listaI[i].setEstadoA()
            else:
               self.__listaI[i].setEstado()
    
    def inciso3(self, curso):
        self.__listaI.sort()
        for i in range(len(self.__listaI)):
            if self.__listaI[i].getEstado() == "R":
                id= self.__listaI[i].getId()
                curso.Listar(id)
                print("Inscripciones Rechazadas")
                print("Dni: {}, \t Apellido: {}, \t\t Nombre: {}, \t\t\tProv:{}".format(self.__listaI[i].getDni(), self.__listaI[i].getApellido(), self.__listaI[i].getNombre(), self.__listaI[i].getProv()))
    
    def inciso4(self, id ):
        i=0
        while i < len(self.__listaI):
            if self.__listaI[i].getId() == id:
                if self.__listaI[i].getEstado()== "A":
                    print("Dni: {}, Apellido: {}, Nombre: {}, Prov:{}".format(self.__listaI[i].getDni(), self.__listaI[i].getApellido(), self.__listaI[i].getNombre(), self.__listaI[i].getProv()))
            i+=1       