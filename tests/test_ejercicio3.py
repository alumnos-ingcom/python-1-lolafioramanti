################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
En este test se prueba una función que compara dos valores numéricos.
Se probará como se comporta cuando el primer número es mayor, menor, o igual al segundo.
"""

import pytest

from src.ejercicio3 import compara

def test_compara_menor():
    '''
        "numero" es menor que "otro_numero" .
    '''
    numero = 2
    otro_numero = 6
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, int), "El valor debe ser un número entero"
    assert resultado == -1, "ERROR. El resultado no es el esperado cuando 'numero' < 'otro_numero'."
    
def test_compara_igual():
    '''
        "numero" es igual que "otro_numero".
    '''
    numero = 10
    otro_numero = 10
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, int), "El valor debe ser un número entero"
    assert resultado == 0, "ERROR. El resultado no es el esperado cuando 'numero' = 'otro_numero'."
    
def test_compara_mayor():
    '''
        "numero" es mayor que "otro_numero".
    '''
    numero = 20
    otro_numero = 5
    resultado = compara(numero, otro_numero)
    assert isinstance(resultado, int), "El valor debe ser un número entero"
    assert resultado == 1, "ERROR. El resultado no es el esperado cuando 'numero' > 'otro_numero'."
    

