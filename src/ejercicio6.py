################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que a partir de tres variables de tipo entero retorne una tupla con dichos valores ordenados de menor a mayor. Y Viceversa
PRECONDICION: Los valores de entrada deben ser números enteros.
POSTCONDICION: Los valores de salida deben ser números enteros ordenados de mayor a menor y viceversa.
"""

################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que a partir de tres variables de tipo entero retorne una tupla con dichos valores ordenados de menor a mayor. Y Viceversa
PRECONDICIÓN: Los valores deben ser números enteros.
POSTCONDICIÓN: Los valores deben ser enteros ordenados de menor a mayor y viceversa.
"""

def ordenar_mayor_a_menor(uno, dos, tres):
    ''' Esta función ordena los números de mayor a menor y los guarda en una lista. '''
    if uno > dos and dos > tres :
        valorMm = [uno, dos, tres]
    elif uno > tres and tres > dos :
        valorMm = [uno, tres, dos]
    elif dos > uno and uno > tres :
        valorMm = [dos, uno, tres]
    elif dos > tres and tres > uno :
        valorMm = [dos, tres, uno]
    elif tres > uno and uno > dos :
        valorMm = [tres, uno, dos]
    elif tres > dos and dos > uno :
        valorMm = [tres, dos, uno]
    valorMm = tuple(valorMm)
    return valorMm
def ordenar_menor_a_mayor(uno, dos, tres):
    ''' Esta función ordena los números de menor a mayor y los guarda en una lista. '''
    if uno < dos and dos < tres :
        valormM = [uno, dos, tres]
    elif uno < tres and tres < dos :
        valormM = [uno, tres, dos]
    elif dos < uno and uno < tres :
        valormM = [dos, uno, tres]
    elif dos < tres and tres < uno :
        valormM = [dos, tres, uno]
    elif tres < uno and uno < dos :
        valormM = [tres, uno, dos]
    elif tres < dos and dos < uno :
        valormM = [tres, dos, uno]
    valormM = tuple(valormM)
    return valormM
def principal():
    """
    Esta función interactúa con el usuario y está a cargo de trabajar con la entrada, las funciones y la salida del programa. '''
    """
    uno = int(input("Ingrese un número: "))
    dos = int(input("Ingrese un número: "))
    tres = int(input("Ingrese un número: "))
    m_a_M = ordenar_menor_a_mayor(uno, dos, tres)
    M_a_m = ordenar_mayor_a_menor(uno, dos, tres)
    print(f"{m_a_M}")
    print(f"{M_a_m}")

if __name__ == "__main__":
    principal()
