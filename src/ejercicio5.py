################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que mediante restas sucesivas, obtenga el valor del cociente y resto de dos números enteros.
PRECONDICIONES: Los valores de entrada deben ser dos números enteros.
POSTCONDIONES: El valor de salida deben un mensaje con dos números, siendo que la cuenta fue exitosa.
"""

def signos(numero):
    if numero != 0:
        suma = numero + abs(numero)
        resta = numero - abs(numero)
        if resta == 0:
            resultado = 1
        else:
            resultado = -1
    else:
        resultado = 0
    return resultado

def division_lenta(dividendo, divisor, signo):
    ''' Función que realiza una resta sucesiva hasta obtener el cociente y resto de dos números. También se multiplica el cociente por el signo original de los valores si es necesario. '''
    cociente = 0
    dividendo = abs(dividendo)
    divisor = abs(divisor)
    if divisor != 0:
        if dividendo >= divisor:
            while (dividendo - divisor) >= 0:
                resto = dividendo - divisor
                cociente += 1
                dividendo = resto
        else:
            resto = dividendo * signo
    else:
        print("No es posible realizar el cálculo con divisor 0.")
    cociente *= signo
    return cociente, resto

def principal():
    ''' Función con la que interactúa el usuario. Obtiene los valores de entrada, ejecuta las dos funciones definidas y se encarga de imprimir la salida. '''
    dividendo = int(input("Ingrese el dividendo: "))
    numero = dividendo
    signo_dividendo = signos(numero)
    divisor = int(input("Ingrese el divisor: "))
    numero = divisor
    signo_divisor = signos(numero)
    signo = signo_divisor * signo_dividendo
    cociente, resto = division_lenta(dividendo, divisor, signo)
    print(f"Cociente {cociente} y resto {resto}")
if __name__ == "__main__":
    principal()
