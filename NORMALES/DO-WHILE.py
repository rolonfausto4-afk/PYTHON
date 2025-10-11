#zona de funciones
def pedir():
    print("digite la 'A' para actualizar sistema")
    print("digite la 'E' para eliminar catalogo")
    print("digite la 'C' para crear catalogo")
    print("digite la 'S' para salir del programa")
    letra=str(input())
    return letra

def procesar(letra):
    while True:
        letra=pedir()
        if letra=="S" or letra=="s":
            proceso=("operacion terminada \n")
            break
        else:
            proceso=("sigue en la operacion DO WHILE \n")
    return proceso

def arrojar(proceso):
    print(proceso)

#zona principal
letra=0
proceso=procesar(letra)
arrojar(proceso)
print("el do while ha finalizado \n")