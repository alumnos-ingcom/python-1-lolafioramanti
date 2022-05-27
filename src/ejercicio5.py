################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que mediante restas sucesivas, obtenga el valor del cociente y resto de dos números enteros.
PRECONDICIONES: Los valores de entrada deben ser dos números enteros, siendo el primero mayor o igual al segundo.
POSTCONDIONES: El valor de salida deben un mensaje con dos números, siendo que la cuenta fue exitosa.
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

def division_lenta(dividendo, divisor, signo):
    ''' Función que realiza una resta sucesiva hasta obtener el cociente y resto de dos números. También se multiplica el cociente por el signo original de los valores si es necesario. '''
    cociente = 0
    while dividendo >= divisor:
        resto = dividendo - divisor
        cociente += 1
        dividendo = resto
    cociente *= signo
    return cociente, resto   
def principal():
    ''' Función con la que interactúa el usuario. Obtiene los valores de entrada, ejecuta las dos funciones definidas y se encarga de imprimir la salida. '''
    dividendo = int(input("Ingrese el dividendo: "))
    divisor = int(input("Ingrese el divisor: "))
    dividendo, divisor, original_dividendo, original_divisor, signo = valor_absoluto(dividendo, divisor)
    cociente_cuenta, resto_cuenta = division_lenta(dividendo, divisor, signo)
    print(f"La cuenta {original_dividendo} / {original_divisor} tiene como cociente {cociente_cuenta} y resto {resto_cuenta}")
if __name__ == "__main__":
    principal()