################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Este test probarán las funciones que ordenan 3 números de mayor a menor (y viceversa).
Se probarán con números positivos, negativos y neutros, además de iguales.
"""
import pytest

from src.ejercicio6 import ordenar_mayor_a_menor, ordenar_menor_a_mayor

def test_ordenar_mayor_a_menor_12_3():
    ''' el orden de mayor a menor será: uno >= dos >= tres '''
    uno = 3
    dos = -4
    tres = -4
    resultado = ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(resultado, tuple), "el resultado debe ser tuple"
    assert resultado == (3, -4, -4), "ERROR. El resultado no es el esperado cuando uno > dos = tres"
    
def test_ordenar_mayor_a_menor_132():
    ''' el orden de mayor a menor será: uno >= tres >= dos '''
    uno = 9
    dos = 4
    tres = 7
    resultado = ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(resultado, tuple), "el resultado debe ser tuple"
    assert resultado == (9, 7, 4), "ERROR. El resultado no es el esperado cuando uno > tres > dos"
    
def test_ordenar_mayor_a_menor_213():
    ''' el orden de mayor a menor será: dos >= uno >= tres '''
    uno = 2
    dos = 5
    tres = -2
    resultado = ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(resultado, tuple), "el resultado debe ser tuple"
    assert resultado == (5, 2, -2), "ERROR. El resultado no es el esperado cuando dos > uno > tres"
    
def test_ordenar_mayor_a_menor_2_31():
    ''' el orden de mayor a menor será: dos >= tres >= uno '''
    uno = 4
    dos = 5
    tres = 5
    resultado = ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(resultado, tuple), "el resultado debe ser tuple"
    assert resultado == (5, 5, 4), "ERROR. El resultado no es el esperado cuando dos = tres > uno"
    
def test_ordenar_mayor_a_menor_31_2():
    ''' el orden de mayor a menor será: tres >= uno >= dos '''
    uno = 5
    dos = 5
    tres = 20
    resultado = ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(resultado, tuple), "el resultado debe ser tuple"
    assert resultado == (20, 5, 5), "ERROR. El resultado no es el esperado cuando tres > uno = dos"

def test_ordenar_mayor_a_menor_321():
    ''' el orden de mayor a menor será: tres >= dos >= uno '''
    uno = -7
    dos = -6
    tres = -5
    resultado = ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(resultado, tuple), "el resultado debe ser tuple"
    assert resultado == (-5, -6, -7), "ERROR. El resultado no es el esperado cuando tres > dos > uno"



def test_ordenar_menor_a_mayor_123():
    ''' el orden de menor a mayor será: uno <= dos <= tres '''
    uno = 0
    dos = 0
    tres = 0
    resultado = ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(resultado, tuple), "el resultado debe ser tuple"
    assert resultado == (0, 0, 0), "ERROR. El resultado no es el esperado cuando uno = dos = tres"
    
def test_ordenar_menor_a_mayor_1_32():
    ''' el orden de menor a mayor será: uno <= tres <= dos '''
    uno = 4
    dos = 7
    tres = 4
    resultado = ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(resultado, tuple), "el resultado debe ser tuple"
    assert resultado == (4, 4, 7), "ERROR. El resultado no es el esperado cuando uno = tres < dos"
    
def test_ordenar_menor_a_mayor_21_3():
    ''' el orden de menor a mayor será: dos <= uno <= tres '''
    uno = -2
    dos = -5
    tres = -2
    resultado = ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(resultado, tuple), "el resultado debe ser tuple"
    assert resultado == (-5, -2, -2), "ERROR. El resultado no es el esperado cuando dos < uno = tres"
    
def test_ordenar_menor_a_mayor_231():
    ''' el orden de menor a mayor será: dos <= tres <= uno '''
    uno = 1
    dos = -6
    tres = 0
    resultado = ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(resultado, tuple), "el resultado debe ser tuple"
    assert resultado == (-6, 0, 1), "ERROR. El resultado no es el esperado cuando dos < tres < uno"
    
def test_ordenar_menor_a_mayor_312():
    ''' el orden de menor a mayor será: tres <= uno <= dos '''
    uno = 8
    dos = 9
    tres = -7
    resultado = ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(resultado, tuple), "el resultado debe ser tuple"
    assert resultado == (-7, 8, 9), "ERROR. El resultado no es el esperado cuando tres < uno < dos"
    
def test_ordenar_menor_a_mayor_321():
    ''' el orden de menor a mayor será: tres <= dos <= uno '''
    uno = 8
    dos = 5
    tres = 3
    resultado = ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(resultado, tuple), "el resultado debe ser tuple"
    assert resultado == (3, 5, 8), "ERROR. El resultado no es el esperado cuando tres < dos < uno"
