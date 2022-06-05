################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Este test pondrá a prueba una función que se encarga de listar los factores primos de un número.
Se probará con valores positivos, negativos, neutros
"""

import pytest

from src.ejercicio9 import factores_primos

def test_factores_primos_positivo():
    numero = 5
    resultado = factores_primos(numero)
    assert isinstance(resultado, tuple), "ERROR, el resultado debe ser del tipo tuple"
    assert resultado == (5,), "ERROR, el resultado debe ser 5"
    
def test_factores_primos_negativo():
    numero = -9
    resultado = factores_primos(numero)
    assert isinstance(resultado, tuple), "ERROR, el resultado debe ser del tipo tuple"
    assert resultado == ('indefinido, este programa funciona sólo con números positivos',), "ERROR, el resultado debe ser 'indefinido' porque el programa no lo puede procesar"
    
def test_factores_primos_neutro():
    numero = 0
    resultado = factores_primos(numero)
    assert isinstance(resultado, tuple), "ERROR, el resultado debe ser tipo tuple"
    assert resultado == ("ninguno",), "ERROR, el número 0 no tiene factores primos"