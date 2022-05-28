################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si un número entero es multiplo de otro, utilizando sumas y restas.
PRECONDICIONES: Los valores de entrada deben ser números enteros.
POSTCONDICIONES: El valor de salida debe ser del tipo booleano.
"""

def valor_absoluto(dividendo, divisor):
    ''' Función que cambia los numeros negativos por su valor absoluto, guarda el signo en una variable y el número original. '''
    if dividendo < 0 and divisor < 0:
        orig_dividendo = dividendo
        dividendo = abs(dividendo)
        orig_divisor = divisor
        divisor = abs(divisor)
        signo = 1
    elif divisor < 0:
        orig_divisor = divisor
        orig_dividendo = dividendo
        divisor = abs(divisor)
        signo = -1
    elif dividendo < 0:
        orig_dividendo = dividendo
        orig_divisor = divisor
        dividendo = abs(dividendo)
        signo = -1
    elif dividendo > 0 and divisor > 0:
        orig_dividendo = dividendo
        orig_divisor = divisor
        signo = 1
    return dividendo, divisor, orig_dividendo, orig_divisor, signo

def es_multiplo(numero, multiplo):
    '''Esta función se encarga de hacer una resta sucesiva para corroborar si un número es múltiplo de otro.'''
    if numero < multiplo:
        valor = False
    else:
        while numero >= multiplo:
            numero -= multiplo
            resto = numero
            if resto == 0:
                valor = True
            else:
                valor = False
    return valor
    
def principal():
    '''Esta función se encarga de interactuar con el usuario. Utiliza la entrada, funciones y salida del algoritmo.
    Su función es preguntar los valores de entrada, llamar a la ejecución de funciones y devolver un valor booleano.'''
    numero = int(input("Ingrese el número: "))
    multiplo = int(input("Ingrese el múltiplo: "))
    dividendo = numero
    divisor = multiplo
    numero, multiplo, numero_original, multiplo_original, signo = valor_absoluto(dividendo, divisor)
    valor = es_multiplo(numero, multiplo)
    print(f"{valor}")
    
if __name__ == "__main__":
    principal()