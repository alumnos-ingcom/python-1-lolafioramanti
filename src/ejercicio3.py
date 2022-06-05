################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:

Retornar -1 si el primero es menor que el segundo
Retornar 0 si son iguales
Retornar 1 si el primero es mayor que el segundo
PRECONDICIONES: El valor de entrada deben ser números reales.
POSTCONDICIÓN: El valor de salida debe ser -1, 0 o 1 según corresponda.
"""

def compara(numero, otro_numero):
    if numero == otro_numero:
        resultado = 0
    else:
        if numero > otro_numero:
            resultado = 1
        else:
            resultado = -1
    return resultado

def principal():
    """
    Indicar si el primer número ingresado por el usuario es menor, igual o mayor al segundo.
    """
    numero = input("Ingrese el primer número: ")
    otro_numero = input("Ingrese el segundo número: ")
    valor = compara(numero, otro_numero)
    print(f"{valor}")
    

if __name__ == "__main__":
    principal()