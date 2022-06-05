################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Este test pone a prueba una función que identifica si un número entero es primo o no.
Para probar se utilizarán números enteros, negativos, primos y no primos.
"""

import pytest

from src.ejercicio8 import es_primo

def test_es_primo_menor2():
    ''' El número es positivo pero menor a 2 '''
    num = 1
    resultado = es_primo(num)
    assert isinstance(resultado, bool), "ERROR, el resultado debe ser un valor booleano"
    assert resultado == False, "ERROR, un número primo debe tener dos divisores positivos distintos"
    
def test_es_primo_negativo():
    ''' El número es negativo. '''
    num = -2
    resultado = es_primo(num)
    assert isinstance(resultado, bool), "ERROR, el resultado debe ser un valor booleano"
    assert resultado == False, "ERROR, el resultado para un número negativo es False"
    
def test_es_primo_ok():
    ''' El número es primo. '''
    num = 2
    resultado = es_primo(num)
    assert isinstance(resultado, bool), "ERROR, el resultado debe ser un valor booleano"
    assert resultado == True, "ERROR, el resultado debe ser un valor booleano"
    
def test_es_primo_no():
    ''' El número no es primo '''
    num = 4
    resultado = es_primo(num)
    assert isinstance(resultado, bool), "ERROR, el resultado debe ser un valor booleano"
    assert resultado == False, "ERROR, a un número divisible por más de dos números positivos distintos le corresponde 'False' "
    