from clientes import Cliente
import csv


class maneCliente:
    __listaC = []

    def __init__(self):
        self.__listaC = []

    def testClien(self):
        archivo = open("clientes.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            dni = fila[0]
            apellido = fila[1]
            nombre = fila[2]
            alias = fila[3]
            uncliente = Cliente(dni, apellido, nombre, alias)
            self.__listaC.append(uncliente)
        archivo.close()

    def incisoA(self, dnix, mcarrito):
        i = 0
        band = True
        while i < len(self.__listaC) and band:
            if self.__listaC[i].getDni() == dnix:
                mcarrito.muestra(self.__listaC[i].getDni())
                print("Nombre:", self.__listaC[i].getNombre())
                print("Apellido:", self.__listaC[i].getApellido())
                print("Alias:", self.__listaC[i].getAlias())
                print("-----------------------")
                band = False
            else:
                print("Error no esta el dni")
                band = False
            i += 1

    def incisoB(self, aliasx, mcarrito):
        i = 0
        band = True
        while i < len(self.__listaC) and band:
            if aliasx == self.__listaC[i].getAlias():
                mcarrito.calcula(self.__listaC[i].getDni())
                print("Alias:", self.__listaC[i].getAlias())
                print("Dni:", self.__listaC[i].getDni())
                band = False
            else:
                print("Error alias no existente")
                band = False
            i += 1
