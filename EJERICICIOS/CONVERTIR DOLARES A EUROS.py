#zona de funciones
def pedir():
    dolar=float(input(print("digite los dolares a convertir")))
    return dolar

def procesar(dolar):
    proceso=(f"la conversion dio como total: {dolar*0.87}")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(dolar):
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                dolar=pedir()
                proceso=procesar(dolar)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")
#zona principal
dolar=0
crear_menu(dolar)
