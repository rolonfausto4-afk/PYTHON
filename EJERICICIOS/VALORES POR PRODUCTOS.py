#zona de funciones
def pedir():
    print("MENU DE HELADOS: \n 1B.VAINILLA \n 2B.CHOCOLATE \n 1C.FRESA \n 2C.CHICLE")
    menu=str(input(print("digite el valor del numero del producto que va llevar")))
    return menu

def procesar(menu):
    menu=menu.upper()
    match menu:
        case "1B":
            proceso=(f"El valor de su numero es {menu} \n por la tanto su producto es: HELADO DE VAINILLA ")
        case "2B":
            proceso=(f"El valor de su numero es {menu} \n por la tanto su producto es: HELADO DE CHOCOLATE")
        case "1C":
            proceso=(f"El valor de su numero es {menu} \n por la tanto su producto es: HELADO DE FRESA")
        case "2C":
            proceso=(f"El valor de su numero es {menu} \n por la tanto su producto es: HELADO DE CHICLE")
        case _:
            proceso=("valor de numero" + menu + "no encontrado")
        
    return proceso

def arrojar(proceso):
    print(proceso)

def crear_menu(menu):
    while True:
        print("1.PEDIR VALORES 2.MENU ANTERIOR 3. SALIR")
        menu=int(input(print("digite el numero segun el menu")))
        match menu:
            case 1:
                menu=pedir()
                proceso=procesar(menu)
            case 2:
                break
            case 3:
                arrojar(proceso)
                break
            case _:
                print("operacion no existente")

#zona principal
menu=0
crear_menu(menu)