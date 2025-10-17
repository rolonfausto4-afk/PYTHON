#zona de funciones
def pedir_base():
    base=int(input(print("digite la longitud")))
    return base

def pedir_altura():
    altura=int(input(print("digite la ancho")))
    return altura

def procesar(base,altura):
    area=(base*altura)
    proceso=("el area del rectangulo es " + str(area))
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(base,altura):
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                base=pedir_base()
                altura=pedir_altura()
                proceso=procesar(base,altura)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principales
base=0
altura=0
crear_menu(base,altura)