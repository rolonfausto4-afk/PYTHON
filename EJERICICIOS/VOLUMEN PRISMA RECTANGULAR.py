#zona de funciones
def definir1():
    longitud=15
    return longitud

def definir2():
    ancho=5
    return ancho

def definir3():
    altura=6
    return altura

def procesar(longitud,ancho,altura):
    proceso=(f"el volumen de prima es: {longitud*ancho*altura}")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(longitud,ancho,altura):
    while True:
        print("1.ESPECIFICAR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                longitud=definir1()
                ancho=definir2()
                altura=definir3()
                proceso=procesar(longitud,ancho,altura)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principal
longitud=0
ancho=0
altura=0
crear_menu(longitud,ancho,altura)