#zona de funciones
def pedir():
    suma=0
    for i in range (0,2,1):
        numeros=float(input(print(f"numero {i+1} para la operacion")))
        suma= suma+numeros
    return suma

def procesar(suma):
    proceso=(f"la suma dio en total {suma}")
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(suma):
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                suma=pedir()
                proceso=procesar(suma)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principal
suma=0
crear_menu(suma)