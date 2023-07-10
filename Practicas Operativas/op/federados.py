class Federado:
    __apellido = " "
    __nombre = " "
    __dni = " "
    __edad = " "
    __club = " "

    def __init__(self, apellido, nombre, dni, edad, club):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__dni = dni
        self.__edad = edad
        self.__club = club

    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre

    def getDni(self):
        return self.__dni

    def getEdad(self):
        return self.__edad

    def getClub(self):
        return self.__club

    def mostrarDatos(self):
        print("---------------")
        print(self.__apellido)
        print(self.__nombre)
        print(self.__dni)
        print(self.__edad)
        print(self.__club)
        print("-----------------")
