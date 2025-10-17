def pedir():
    inch=float(input(print("digite las pulgadas")))
    return inch

def procesar(inch):
    proceso=(f"los centimetros son: {inch*2.54}")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(inch):
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                inch=pedir()
                proceso=procesar(inch)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principal
inch=0
crear_menu(inch)
