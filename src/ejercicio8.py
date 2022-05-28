################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si un numero indicado es Primo.
PRECONDICIÓN: El valor de entrada debe ser un número entero.
POSTCONDICIÓN: El valor de salida debe ser "True" o "False".
"""
def es_primo(num):
    ''' Esta función calcula si el número ingresado es primo o no. Devuelve True o False.'''
    if num < 2:
        return False
    divisor = 2
    while divisor > 1 and divisor < num:
        if num % divisor == 0:
            return False
        else:
            divisor += 1
    return True
    
def principal():
    '''Esta función interactúa con el usuario. Se encarga de obtener la entrada, llamar a la función e imprimir el resultado de la misma.'''
    num = int(input("Ingrese: "))
    respuesta = es_primo(num)
    print(f"{respuesta}")

if __name__ == "__main__":
    principal()