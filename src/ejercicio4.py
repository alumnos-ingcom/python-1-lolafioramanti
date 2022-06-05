################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que haga la suma entre dos números enteros sin hacer la operación de manera directa. Esto quiere decir que para hacer la suma entre 4 y 3, las operaciones resultantes deberán ser 4+1+1+1.

La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.
PRECONDICIONES: los valores de entrada deben ser números enteros.
POSTCONDICIONES: los valores de entrada deben ser números enteros.
"""
def suma_lenta(numero, otro_numero):
    contador = otro_numero
    suma = numero
    if otro_numero < 0:
        while contador < 0:
            suma = suma + (-1)
            contador = contador + 1
    else:
        while contador > 0:
            suma = suma + 1
            contador = contador - 1
    return suma


def principal():
    '''
    Suma lenta de dos números.
    '''
    numero = int(input("Ingrese el primer número: "))
    otro_numero = int(input("Ingrese el segundo número: "))
    resultado = suma_lenta(numero, otro_numero)
    print(f"{resultado}")
    
if __name__ == "__main__":
    principal()