################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.

Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit como un número decimal, utilice esta formula para calcular los grados centígrados y retorne el resultado obtenido. Y viceversa.
PRECONDICIONES: los valores de entrada deben ser números.
POSTCONDICIONES: los valores de salida deben ser números que hayan sido convertidos a los grados correspondientes.
"""

def convertir_a_fahrenheit(centigrados):
    fahrenheit = (centigrados * 1.8 ) + 32
    resultado = fahrenheit
    return resultado

def convertir_a_centigrados(fahrenheit):
    centigrados = (fahrenheit - 32) / 1.8
    resultado = centigrados
    return resultado

def principal():
    """
    Conversión de grados centígrados a fahrenheit, y viceversa.
    """
    centigrados = int(input("Ingrese los grados centígrados a convertir: "))
    conversion1 = convertir_a_fahrenheit(centigrados)
    print(f"{conversion1}ºF")
    fahrenheit = int(input("Ingrese el grado fahrenheit a convertir: "))
    conversion2 = convertir_a_centigrados(fahrenheit)
    print(f"{conversion2}ºC")

if __name__ == "__main__":
    principal()
    