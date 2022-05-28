################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si una palabra o frase ingresada se trata de un palindromo.
Palíndromo, es si se lee igual de derecha a izquierda que de izquierda a derecha.
PRECONDICIÓN: El valor de entrada debe ser una cadena de carácteres.
POSTCONDICIÓN: El valor de salida debe ser "True" o "False".
"""

def es_palindromo(texto):
    '''Función que evalúa si una frase es palíndromo.'''
    if texto == texto[::-1]:
        valor = True
    else:
        valor = False
    return valor

def principal():
    '''Función que interactúa con el usuario y el programa. Se encarga de usar la entrada, función y salida. Devuelve valores booleanos.'''
    texto = input("Ingrese el texto: ")
    resultado = es_palindromo(texto)
    print(f"{resultado}")
    
if __name__ == "__main__":
    principal()