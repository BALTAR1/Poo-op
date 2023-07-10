class Carrito:
    __dni = " "
    __id = " "
    __precio = " "
    __cantidad = " "
    __itempedido = " "

    def __init__(self, dni, id, precio, cantidad, itempedido):
        self.__dni = dni
        self.__id = id
        self.__precio = precio
        self.__cantidad = cantidad
        self.__itempedido = itempedido

    def getDni(self):
        return self.__dni

    def getId(self):
        return self.__id

    def getPrecio(self):
        return self.__precio

    def getCantidad(self):
        return self.__cantidad

    def getitemPedido(self):
        return self.__itempedido

    def __lt__(self, otro):
        return self.__dni < otro.__dni
