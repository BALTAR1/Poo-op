from manejapun import ManejaPun
from manejafed import ManejaFed

if __name__ == "__main__":
    mp = ManejaPun()
    mf = ManejaFed()
    mp.testPun()
    mf.testFed()
    while True:
        print("MENU DE OPCIONES")
        print("Inciso 1")
        print("Inciso 2")
        print("Inciso 3")
        print("Inciso 4")
        print("Salir 5")
        opcion = input("\nIngrese una opcion: ")
        print("-------------------")

        if opcion == "1":
            estilo = str(input("Ingrese un estilo:"))
            edad = int(input("Ingrese una edad:"))
            mp.incisoA(edad, mf, estilo)
        elif opcion == "2":
            mp.incisoB(mf)
        elif opcion == "3":
            mp.incisoC(mf)
        elif opcion == "4":
            dnix = input("Ingrese un dni:")
            estilox = input("Ingrese un estilo:")
            mp.incisoD(dnix, estilox)
        elif opcion == "5":
            break
