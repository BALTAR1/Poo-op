class Puntaje:
    __dnip = " "
    __estilo = " "
    __pun1 = " "
    __pun2 = " "
    __pun3 = " "

    def __init__(self, dnip, estilo, pun1, pun2, pun3):
        self.__dnip = dnip
        self.__estilo = estilo
        self.__pun1 = pun1
        self.__pun2 = pun2
        self.__pun3 = pun3

    def getDnip(self):
        return self.__dnip

    def getEstilo(self):
        return self.__estilo

    def getPun1(self):
        return self.__pun1

    def getPun2(self):
        return self.__pun2

    def getPun3(self):
        return self.__pun3

    def Promedio(self):
        prom = 0
        prom = self.__pun1 + self.__pun2 + self.__pun3
        prom = prom / 3
        return prom

    def __gt__(self, otro):
        return self.Promedio() > otro.Promedio()
