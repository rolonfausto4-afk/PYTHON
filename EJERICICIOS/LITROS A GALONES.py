#zona de funciones
def pedir():
    litro=float(input(print("digite los litros")))
    return litro

def procesar(litro):
    proceso=(f"los galones son: {litro*0.264172}")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(litro):
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                litro=pedir()
                proceso=procesar(litro)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principal
litro=0
crear_menu(litro)