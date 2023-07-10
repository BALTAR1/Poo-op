from federados import Federado
import csv
from manejapun import ManejaPun


class ManejaFed:
    __listafed = []

    def __init__(self):
        self.__listafed = []

    def testFed(self):
        archivo = open("federados.csv")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            apellido = fila[0]
            nombre = fila[1]
            dni = fila[2]
            edad = int(fila[3])
            club = fila[4]
            unfederado = Federado(apellido, nombre, dni, edad, club)
            self.__listafed.append(unfederado)
        archivo.close()
        i = 0
        while i < len(self.__listafed):
            self.__listafed[i].mostrarDatos()
            i += 1

    def busca(self, dni, edad):
        i = 0
        band = True
        while i < len(self.__listafed) and band:
            if edad == self.__listafed[i].getEdad():
                if dni == self.__listafed[i].getDni():
                    print("--------------------------------------------")
                    print("Apellido", self.__listafed[i].getApellido())
                    print("Nombre", self.__listafed[i].getNombre())
                    print("Dni", self.__listafed[i].getDni())
                    print("--------------------------------------------")
                    band = False  # pongo una bandera para que una vez que lo encuentre corte el ciclo
            i += 1  # mando a la funcion estilo del otro manejador el dni de federdos y el estilo

    def listarestilos(self, dni):
        i = 0
        band = True
        while i < len(self.__listafed) and band:
            if dni == self.__listafed[i].getDni():
                print("--------------------------------------------")
                print("Apellido:", self.__listafed[i].getApellido())
                print("Nombre:", self.__listafed[i].getNombre())
                print("Dni:", self.__listafed[i].getDni())
                print("Edad:", self.__listafed[i].getEdad())
                print("--------------------------------------------")
                band = False
            i += 1
