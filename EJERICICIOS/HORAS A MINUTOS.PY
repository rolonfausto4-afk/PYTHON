#zona de funciones
def pedir():
    horas=float(input(print("digite las horas")))
    return horas

def procesar(horas):
    proceso=(f"los minutos son : {horas*60} minutos")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(horas):
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                horas=pedir()
                proceso=procesar(horas)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principal
horas=0
crear_menu(horas)
