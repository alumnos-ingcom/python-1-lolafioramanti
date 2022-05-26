################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que reciba un número e indique si el mismo es positivo, negativo o cero utilizando sumas y restas.
PRECONDICION: El valor de entrada debe ser un número.
POSTCONDICION: El valor de salida debe ser "positivo", "negativo" o "neutro".
"""

def signo(numero):
    if numero != 0:
        suma = numero + abs(numero)
        resta = numero - abs(numero)
        if resta == 0:
            resultado = "positivo"
        else:
            resultado = "negativo"
    else:
        resultado = "neutro"
    return resultado

def principal():
    '''
    Indicar el signo de un número usando sumas y restas.
    '''
    numero = float(input("Ingrese número: "))
    valor = signo(numero)
    print(f"{valor}")
    
if __name__ == "__main__":
    principal()