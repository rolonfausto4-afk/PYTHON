#zona de funciones
def pedir():
    num_f=int(input(print("digite numeros del 1 al 12")))
    return num_f

def procesar(num):
    match num:
        case 1:
            proceso_f=("enero")
        case 2:
            proceso_f=("febrero")
        case 3:
            proceso_f=("marzo")
        case 4:
            proceso_f=("abril")
        case 5:
            proceso_f=("mayo")
        case 6:
            proceso_f=("junio")
        case 7:
            proceso_f=("julio")
        case 8:
            proceso_f=("agosto")
        case 9:
            proceso_f=("septiembre")
        case 10:
            proceso_f=("octubre")
        case 11:
            proceso_f=("noviembre")
        case 12:
            proceso_f=("diciembre")
        case _:
            proceso_f=("no existe mes")
    return proceso_f

def imprimir(proceso):
        print(proceso)
        
#zona principal
num=pedir()
proceso=procesar(num)
imprimir(proceso)



    