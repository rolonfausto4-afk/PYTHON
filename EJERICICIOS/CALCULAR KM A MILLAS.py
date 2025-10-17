#zona de funciones
def pedir():
    kilometros=float(input(print("digite los kilometros a convertir")))
    return kilometros

def procesar(kilometros):
    proceso=(f"las millas son: {kilometros*0.621371}")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(kilometros):
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                kilometros=pedir()
                proceso=procesar(kilometros)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")
#zona principal
kilometros=0
crear_menu(kilometros)
