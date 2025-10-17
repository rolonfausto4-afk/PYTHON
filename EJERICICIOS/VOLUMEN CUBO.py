#zona de funciones
def pedir():
    cubo=float(input(print("digite el lado del cubo")))
    return cubo

def procesar(cubo):
    proceso=(f"el volumen del cubo es: {cubo**3}")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(cubo):
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                cubo=pedir()
                proceso=procesar(cubo)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principal
cubo=0
crear_menu(cubo)