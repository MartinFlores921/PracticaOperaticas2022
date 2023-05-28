import csv
from personal import Personal
class manejadorP:
    __listaP: list
    
    def __init__(self):
        self.__listaP = []
    
    
    def cargarListaP(self):
        archivo= open("personal.csv")
        reader= csv.reader(archivo, delimiter=";")
        next (reader)
        for fila in reader:
            sueldoTotal= int(fila[5]) if len(fila) > 5 else 0
            unPersonal = Personal(fila[0], fila[1], fila[2], fila[3], int(fila[4]), sueldoTotal)
            self.__listaP.append(unPersonal)
        archivo.close()
    
    def mostrarListaP(self):
        for i in range(len(self.__listaP)):
            print("Apellido{}, Nombre:{},  Dni: {}, Legajo: {}, SueldoBasico: {}, SueldoACobrar: {}".format(self.__listaP[i].getApellido(),self.__listaP[i].getNombre(), self.__listaP[i].getDni(), self.__listaP[i].getLegajo(), self.__listaP[i].getSueldoBasico(), self.__listaP[i].getSueldoTotal()))
    
    """def inciso1(self, leg, novedad):
        i=0
        while i < len(self.__listaP):
            if self.__listaP[i].getLegajo() == leg:
                legajo= self.__listaP[i].getLegajo()
                desc= novedad.ObtenerDescuento(legajo)
                aum= novedad.ObtenerAumento(legajo)
                self.__listaP[i].ActualizarSueldo(desc, aum)
            i+=1
        print("El Sueldo a Cobrar para el legago: {} es de: {}".format(leg, ))"""
    
    def Actualizar(self, novedad):
        for i in range(len(self.__listaP)):
            legajo= self.__listaP[i].getLegajo()
            desc= novedad.ObtenerDescuento(legajo)
            aum= novedad.ObtenerAumento(legajo)
            self.__listaP[i].ActualizarSueldo(desc, aum)
    
    def inciso1(self, legajo):
        i=0
        while i < len(self.__listaP):
            if self.__listaP[i].getLegajo() == legajo:
                print("El sueldo a Cobrar para el Legajo {} es: {}".format(legajo, self.__listaP[i].getSueldoTotal()))
            i+=1
    def mostrar(self, novedad):
        self.__listaP.sort()
        for i in range(len(self.__listaP)):
            leg= self.__listaP[i].getLegajo()
            print("Apellido: {}  \t Nombre: {}".format(self.__listaP[i].getApellido(), self.__listaP[i].getNombre()))
            print("Dni:{}".format(self.__listaP[i].getDni()))
            print("Sueldo Basico: {}".format(self.__listaP[i].getSueldoBasico()))
            novedad.mostrar(leg)
            print("Sueldo a Cobrar: {}".format(self.__listaP[i].getSueldoTotal()))
            
        
    
    def inciso3(self):
        min= self.__listaP[0].getSueldoTotal()
        for i in range(len(self.__listaP)):
            if self.__listaP[i].getSueldoTotal() < min:
                min= self.__listaP[i].getSueldoTotal()
        print("El Sueldo a Cobrar mas Bajo es: {}".format(min))