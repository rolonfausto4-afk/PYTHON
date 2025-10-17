#zona de funciones
def pedir():
    cuadrado=float(input(print("digite el lado del cuadrado")))
    return cuadrado

def procesar(cuadrado):
    proceso=(f"el area del cuadrado es: {cuadrado**2}")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(cuadrado):
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                cuadrado=pedir()
                proceso=procesar(cuadrado)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principal
cuadrado=0
crear_menu(cuadrado)
