from carrito import Carrito
import csv


class maneCarrito:
    __listaCarrito = []

    def __init__(self):
        self.__listaCarrito = []

    def testCarrito(self):
        archivo = open("carritoCompras.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            dni = fila[0]
            id = fila[1]
            precio = int(fila[2])
            cantidad = int(fila[3])
            itempedido = fila[4]
            uncarrito = Carrito(dni, id, precio, cantidad, itempedido)
            self.__listaCarrito.append(uncarrito)
        archivo.close()

    def muestra(self, dni):
        i = 0
        while i < len(self.__listaCarrito):
            if self.__listaCarrito[i].getDni() == dni:
                print("Precio:", self.__listaCarrito[i].getCantidad())
                print("Cantidad:", self.__listaCarrito[i].getPrecio())
                print("ItemPedido:", self.__listaCarrito[i].getitemPedido())
                print(
                    "Total:",
                    self.__listaCarrito[i].getPrecio()
                    * self.__listaCarrito[i].getCantidad(),
                )
                print("------------------------------")
            i += 1

    def calcula(self, dni):
        i = 0
        x = 0
        band = True
        while i < len(self.__listaCarrito):
            if dni == self.__listaCarrito[i].getDni() and band:
                x = (
                    self.__listaCarrito[i].getCantidad()
                    * self.__listaCarrito[i].getPrecio()
                )
            i += 1
        print("La suma de sus compras es de:", x)
        if x > 70000:
            print("---------------------------")
            print("CUPON DE DESCUENTO")
            por = 10 * x / 100
            dif = (x - 70000) - por
            print("El descuento a aplicar es de:", por)
            print("El importe a pagar es:", dif)
        else:
            print("El cliente no obtuvo un cupon")

    def ordena(self):
        i = 0
        self.__listaCarrito.sort()
        for i in range(len(self.__listaCarrito)):
            print(self.__listaCarrito[i].getDni())
