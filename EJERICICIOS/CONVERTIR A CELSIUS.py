#zona de funciones
def pedir():
    celsius=float(input(print("digite los grados celsius a convertir")))
    return celsius

def procesar(celsius):
    proceso=(f"los grados fahrenheit son: {(9/5*celsius)+32}")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(celsius):
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                celsius=pedir()
                proceso=procesar(celsius)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")
                
#zona principal
celsius=0
crear_menu(celsius)
