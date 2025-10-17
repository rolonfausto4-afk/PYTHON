def definir1():
    altura=10
    return altura

def definir2():
    ancho=12
    return ancho

def definir3():
    largo=5
    return largo

def procesar(largo,ancho,altura):
    proceso=(f"el volumen de la piramide es: {(1/3)*(largo*ancho*altura)/3}")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(largo,ancho,altura):
    while True:
        print("1.ESPECIFICAR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                largo=definir1()
                ancho=definir2()
                altura=definir3()
                proceso=procesar(largo,ancho,altura)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principal
altura=0
ancho=0
largo=0
crear_menu(largo,ancho,altura)