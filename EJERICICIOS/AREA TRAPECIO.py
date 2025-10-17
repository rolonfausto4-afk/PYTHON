#zona de funciones
def definir1():
    base_mayor=10
    return base_mayor

def definir2():
    base_menor=12
    return base_menor

def definir3():
    altura=5
    return altura

def procesar(base_mayor,base_menor,altura):
    proceso=(f"el area del trapecio es: {(base_mayor+base_menor)*altura/2}")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(base_mayor,base_menor,altura):
    while True:
        print("1.ESPECIFICAR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                base_mayor=definir1()
                base_menor=definir2()
                altura=definir3()
                proceso=procesar(base_mayor,base_menor,altura)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principal
base_mayor=0
base_menor=0
altura=0
crear_menu(base_mayor,base_menor,altura)