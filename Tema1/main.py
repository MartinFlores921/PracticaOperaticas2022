


from manejadorPersonal import manejadorP
from manejadorNovedad import manejadorN

if __name__ == '__main__':
    personal= manejadorP()
    personal.cargarListaP()
    novedad= manejadorN()
    novedad.cargarListaN()
    print("A continuacion se mostrara la Lista Personal: \n")
    personal.mostrarListaP()
    print("A continuacion se mostrara la Lista Novedad: \n")
    novedad.mostrarListaN()
    print("INCISO 1 \n")
    personal.Actualizar(novedad)
    leg= input("Ingrese el legajo de un personal \n")
    personal.inciso1(leg)
    #personal.mostrarListaP()
    print("INCISO 2 \n")
    personal.mostrar(novedad)
    
    print("INCISO 3 \n")
    personal.inciso3()