import math
#zona de funciones
def pedir(i):
    numero=float(input(print(f"digite el numero {i} para la operacion")))
    return numero

def definir():
    n1=pedir(1)
    n2=pedir(2)

    division=n1/n2
    return division

def procesar(division):
    proceso=(f"el conciente entero es: {math.trunc(division)}")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(division):
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                division=definir()
                proceso=procesar(division)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principal
division=0
crear_menu(division)