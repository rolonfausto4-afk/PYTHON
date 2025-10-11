#zona de funciones
def pedir(i):
    print("digite el numero: "+ str(i+1) + " para la suma")
    num=float(input())
    return num

def procesar(num):
    suma=float(0)
    for i in range(0,10,1):
        num=pedir(i)
        suma=suma+num
    return suma

def arrojar(suma):
    print("suma es igual a:" + str(suma))

#zona principal
num=float(0)
suma=procesar(num)
arrojar(suma)
