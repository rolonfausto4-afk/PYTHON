#Zona de funciones
def numero_a_dar():  
    numero=int(input(print("digite un numero")))
    return numero

def procesar_codigo(numero):
    procesar=("numero: "+ str(numero) +" es: ")
    return procesar

def arrojar(procesar):
    if numero>0:
        print(procesar + "es positivo")
    elif numero<0:
        print(procesar + "es negrativo")
    else:
        print(procesar + "es neutro")

#principal
numero=numero_a_dar()
procesar= procesar_codigo(numero)
arrojar(procesar)
