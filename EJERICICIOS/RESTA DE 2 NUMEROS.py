#zona de funciones
def pedir(i):
    numero=float(input(print(f"digite el numero {i} para la operacion")))
    return numero

def definir():
    n1=pedir(1)
    n2=pedir(2)

    resta=n1-n2
    return resta

def procesar(resta):
    proceso=(f"la resta dio en total {resta}")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(resta):
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                resta=definir()
                proceso=procesar(resta)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principal
resta=0
crear_menu(resta)