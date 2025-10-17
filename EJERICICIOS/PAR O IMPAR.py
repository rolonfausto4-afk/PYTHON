def pedir():
    numero=float(input(print("digite el numero")))
    return numero

def procesar(numero):
    if numero%2==0:
        proceso=("el numero es par")
    else:
        proceso=("el numero es impar")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(numero):
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                numero=pedir()
                proceso=procesar(numero)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principal
numero=0
crear_menu(numero)
