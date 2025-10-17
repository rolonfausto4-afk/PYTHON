#zona de funciones
def pedir():
    lado=float(input(print("digite un lado del hexagono")))
    return lado

def procesar(lado):
    proceso=(f"el area del hexagono es: {(lado*6)*(((lado)*(3**(1/2)))/2)/2}")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(lado):
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                lado=pedir()
                proceso=procesar(lado)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principal
lado=0
crear_menu(lado)