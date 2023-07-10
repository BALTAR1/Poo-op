from puntaje import Puntaje
import csv


class ManejaPun:
    __listaPun = []

    def __init__(self):
        self.__listaPun = []

    def testPun(self):
        archivo = open("evaluacion.csv")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            dnip = fila[0]
            estilo = fila[1]
            pun1 = float(fila[2])
            pun2 = float(fila[3])
            pun3 = float(fila[4])
            unpuntaje = Puntaje(dnip, estilo, pun1, pun2, pun3)
            self.__listaPun.append(unpuntaje)
        archivo.close()

    def incisoA(self, edad, mf, estilo):
        i = 0
        # band = False     * esto no lo usas en ningun momento
        while i < len(self.__listaPun):
            if estilo == self.__listaPun[i].getEstilo():
                mf.busca(
                    self.__listaPun[i].getDnip(), edad
                )  #  *no hace falta una condicion aqui
            # if mf.busca(self.__listaPun[i].getDnip(), edad):
            # i += 1   *esto esta en vano
            i += 1

    def incisoB(self, mf):
        i = 0
        max = 0.0
        while i < len(self.__listaPun):
            if self.__listaPun[i].Promedio() > max:
                max = self.__listaPun[i].Promedio()
                aux = self.__listaPun[i]
            i += 1
        mf.muestra(aux.getDnip())
        print(aux.getEstilo())

    def incisoC(self, mf):
        i = 0
        j = 0
        band = True
        while i < len(self.__listaPun):
            j = 0
            band = True
            if self.__listaPun[i].getEstilo() == "l":
                dni = self.__listaPun[i].getDnip()
                while j < len(self.__listaPun) and band:
                    if (
                        self.__listaPun[j].getDnip() == dni
                        and self.__listaPun[j].getEstilo() == "e"
                    ):
                        mf.listarestilos(dni)
                        band = False
                    j += 1
            i += 1
        # Si razonas esta logica estas picado, pero no es dificil, solo presta atencio que hace cada linea

    def incisoD(self, dnix, estilox):
        i = 0
        while i < len(self.__listaPun):
            if dnix == self.__listaPun[i].getDnip():
                if estilox == self.__listaPun[i].getEstilo():
                    print(self.__listaPun[i].getPun1())
                    print(self.__listaPun[i].getPun2())
                    print(self.__listaPun[i].getPun3())
            i += 1
