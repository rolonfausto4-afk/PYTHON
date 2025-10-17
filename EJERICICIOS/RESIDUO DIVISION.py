#zona de funciones
def pedir(mensaje):
    numero=float(input(mensaje))
    print(mensaje)
    return numero

def definir():
    n1=pedir("digite el dividendo")
    n2=pedir("digite el divisor")

    residuo=n1%n2
    return residuo

def procesar(residuo):
    proceso=(f"la residuo dio en total {residuo}")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(residuo):
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                residuo=definir()
                proceso=procesar(residuo)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principal
residuo=0
crear_menu(residuo)