#zona de funciones
def pedir_ancho():
    ancho=int(input(print("digite el longitud")))
    return ancho

def pedir_largo():
    largo=int(input(print("digite el ancho")))
    return largo

def procesar(ancho,largo):
    area=(ancho*largo)
    proceso=("el area del rectangulo es " + str(area))
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(ancho,largo):
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                ancho=pedir_ancho()
                largo=pedir_largo()
                proceso=procesar(ancho,largo)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principales
ancho=0
largo=0
crear_menu(ancho,largo)