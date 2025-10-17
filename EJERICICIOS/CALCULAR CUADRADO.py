#zona de funciones
def pedir():
    num=int(input(print("digite el numero para la operacion")))
    numero_cuadrado=num**2
    return numero_cuadrado

def procesar(numero_cuadrado):
    proceso=(f"el cuadrado del numero dio en total {numero_cuadrado}")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(numero_cuadrado):
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                numero_cuadrado=pedir()
                proceso=procesar(numero_cuadrado)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principal
numero_cuadrado=0
crear_menu(numero_cuadrado)