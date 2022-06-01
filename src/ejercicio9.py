################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que retorne una tuple con factores primos de un numero entero positivo.
PRECONDICION: El valor de entrada debe ser un entero positivo.
POSTCONDICION: El valor de salida debe ser en formato tuple.
"""

def factores_primos(numero):
    '''Esta función se encarga de encontrar los factores primos de un número.'''
    divisor = 2
    factores = []
    if numero == 0:
        factores.append("ninguno")
    elif numero < 0:
        factores.append("indefinido, este programa funciona sólo con números positivos")
    else:
        while numero > 1:
            if numero % divisor != 0:
                divisor += 1
        else:
            numero = numero // divisor
            factores.append(divisor)
    tupla = tuple(factores)
    return tupla
        
def principal():
    '''Esta función se encarga de interactuar con el usuario.
    Pide un número como entrada, lo conecta con la función, e imprime como salida una tuple.'''
    numero = int(input("Ingrese un número: "))
    factores = factores_primos(numero)
    print(f"Los factores primos son {factores}")

if __name__ == "__main__":
    principal()
    
