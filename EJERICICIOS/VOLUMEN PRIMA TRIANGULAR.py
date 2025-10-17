#zona de funciones
def definir1():
    altura=10
    return altura

def definir2():
    ancho=12
    return ancho

def definir3():
    longitud=5
    return longitud

def definir4():
    ancho= definir2()
    longitud= definir3()
    area=ancho*longitud
    return area

def procesar(altura,area):
    proceso=(f"el area del prisma triangular es: {area} \n y volumen del prima es {area*altura}")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(altura,area):
    while True:
        print("1.ESPECIFICAR VAlongitudRES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                altura=definir1()
                area=definir4()
                proceso=procesar(altura,area)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principal
altura=0
area=0
crear_menu(altura,area)