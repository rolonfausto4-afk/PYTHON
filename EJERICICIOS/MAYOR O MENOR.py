#zona de funciones
def pedir(i):
    numero=float(input(print(f"digite el numero {i} para la operacion")))
    return numero

def procesar(num1,num2):
    num1= pedir(1)
    num2= pedir(2)
    if num1>num2:
        proceso=(f"{num1} es mayor que {num2}")
    elif num2>num1:
        proceso=(f"{num2} es menor que {num1}")
    else:
        proceso="numeros son iguales"
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu():
    num1=0
    num2=0
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                proceso=procesar(num1,num2)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principal
crear_menu()