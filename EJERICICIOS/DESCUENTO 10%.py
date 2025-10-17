#zona de funciones
def pedir():
    num=float(input(print("digite el numero para el descuento")))
    return num

def procesar(num):
    proceso=(f" numero: {num}\n 10% de descuento: {num*0.10}\n numero despues del descuento: {num*0.90}")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(num):
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                num=pedir()
                proceso=procesar(num)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principal
num=0
crear_menu(num)