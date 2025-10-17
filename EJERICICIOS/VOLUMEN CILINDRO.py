import math
#zona de funciones
def definir1():
    radio=float(5)
    return radio

def definir2():
    altura=float(10)
    return altura

def procesar(radio,altura):
    proceso=(f"el volumen del cilindro es: {(math.pi)*(radio**2)*(altura)}")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(radio,altura):
    while True:
        print("1.ESPECIFICAR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                radio=definir1()
                altura=definir2()
                proceso=procesar(radio,altura)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principal
radio=0
altura=0
crear_menu(radio,altura)
