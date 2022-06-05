################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Este test prueba una función de suma lenta (suma indirecta).
Se testeará con enteros positivos y negativos.
"""

import pytest

from src.ejercicio4 import suma_lenta

def test_suma_lenta_p_p():
    '''
        "numero" y "otro_numero" son enteros positivos.
    '''
    numero = 5
    otro_numero = 4
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), "El valor debe ser un número entero"
    assert resultado == 9, "ERROR. El resultado no es el esperado cuando 'numero' y 'otro_numero' son POSITIVOS."
    
def test_suma_lenta_p_n():
    '''
        "numero" es positivo, "otro_numero" es negativo
    '''
    numero = 5
    otro_numero = -3
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), "El valor debe ser un número entero"
    assert resultado == 2, "ERROR. El resultado no es el esperado cuando 'numero' es POSITIVO y 'otro_numero' es NEGATIVO."

def test_suma_lenta_n_p():
    '''
        "numero" es negativo, "otro_numero" es positivo.
    '''
    numero = -4
    otro_numero = 2
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), "El valor debe ser un número entero"
    assert resultado == -2, "ERROR. El resultado no es el esperado cuando 'numero' es NEGATIVO y 'otro_numero' es POSITIVO."
    
def test_suma_lenta_n_n():
    '''
        "numero" y "otro_numero" son negativos.
    '''
    numero = -12
    otro_numero = -8
    resultado = suma_lenta(numero, otro_numero)
    assert isinstance(resultado, int), "El valor debe ser un número entero"
    assert resultado == -20, "ERROR. El resultado no es el esperado cuando 'numero' y 'otro_numero' son NEGATIVOS."