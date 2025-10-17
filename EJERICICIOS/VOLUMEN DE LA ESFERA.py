#zona de funciones
import math
def pedir():
    radio=float(input(print("digite el radio de la esfera")))
    return radio

def procesar(radio):
    volumen=float(1)
    volumen=(4/3)*(math.pi)*(radio**3)
    proceso=("el volumen de esfera es:"+ str(volumen)) 
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(radio):
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
radio=0
crear_menu(radio)