#zona de funciones
def pedir():
    num=int(input(print("digite el numero para la operacion")))
    numero_raiz=num**(1/2)
    return numero_raiz

def procesar(numero_raiz):
    proceso=(f"la raiz cuadrada es {numero_raiz}")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(numero_raiz):
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                numero_raiz=pedir()
                proceso=procesar(numero_raiz)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principal
numero_raiz=0
crear_menu(numero_raiz)