#zona de funciones
def pedir():
    libra=float(input(print("digite las libras")))
    return libra

def procesar(libra):
    proceso=(f"los kilogramos son: {libra*0.453592}")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(libra):
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                libra=pedir()
                proceso=procesar(libra)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principal
libra=0
crear_menu(libra)