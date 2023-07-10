class Cliente:
    __dni = " "
    __apellido = " "
    __nombre = " "
    __alias = " "

    def __init__(self, dni, apellido, nombre, alias):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__alias = alias

    def getDni(self):
        return self.__dni

    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre

    def getAlias(self):
        return self.__alias
