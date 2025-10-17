#zona de funciones
import math
def pedir():
    radio=float(input(print("digite el radio del circulo")))
    return radio

def procesar(radio):    
    proceso=(f"el area del circulo es: {(math.pi)*(radio**2)}") 
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(radio,proceso):
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                radio=pedir()
                proceso=procesar(radio)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")
#zona principal
cuadrado=0
radio=0
crear_menu(cuadrado,radio)