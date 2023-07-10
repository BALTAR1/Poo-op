from maneCliente import maneCliente
from maneCarrito import maneCarrito

if __name__ == "__main__":
    mc = maneCliente()
    mc.testClien()
    mcarrito = maneCarrito()
    mcarrito.testCarrito()

    print("MENU DE OPCIONES")
    print("Inciso A")
    print("Inciso B")
    print("Inciso C")
    print("Ingrese'F'para finalizar")
    opcion = input("\nIngrese una opcion:")

    while opcion != "F":
        if opcion == "A":
            dnix = input("Ingrese un dni de un cliente:")
            mc.incisoA(dnix, mcarrito)

        elif opcion == "B":
            aliasx = input("Ingrese un alias de un cliente:")
            mc.incisoB(aliasx, mcarrito)

        elif opcion == "C":
            mcarrito.ordena()
