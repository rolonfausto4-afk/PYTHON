#zona de funciones
def pedir():
    print("Digite un numero: ")
    num=int(input())
    return num

def procesar(num):
    while num!=0:
        num=pedir()
        arrojar(num)
    proceso=("operacion finalizada")
    return proceso

def arrojar(num):
    if num==0:
        print("numero neutro")
    elif num%2==0:
        print("numero es par")
    else:
        print("numero es impar")

def arrojar2(proceso):
    print(proceso)

#zona principal
num=int(1)
proceso=procesar(num)
arrojar2(proceso)