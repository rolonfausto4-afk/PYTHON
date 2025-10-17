#zona de funciones
def pedir():
    valor_cuenta=float(input(print("digite el dinero en su cuenta")))
    return valor_cuenta

def procesar(valor_cuenta):
    proceso=(f"los intereses del 5% reflejados en su cuenta son de {valor_cuenta*0.05}")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(valor_cuenta):
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                valor_cuenta=pedir()
                proceso=procesar(valor_cuenta)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principal
valor_cuenta=0
crear_menu(valor_cuenta)
