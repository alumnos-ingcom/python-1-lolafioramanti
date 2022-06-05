################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si un número entero es multiplo de otro, utilizando sumas y restas.
PRECONDICIONES: Los valores de entrada deben ser números enteros.
POSTCONDICIONES: El valor de salida debe ser del tipo booleano.
"""

def es_multiplo(numero, multiplo):
    '''Esta función se encarga de hacer una resta sucesiva para corroborar si un número es múltiplo de otro.'''
    if multiplo == 0:
        valor = False
    else:
        if numero < 0:
            numero *= -1
        if multiplo < 0:
            multiplo *= -1
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
    valor = es_multiplo(numero, multiplo)
    print(f"{valor}")
    
if __name__ == "__main__":
    principal()
