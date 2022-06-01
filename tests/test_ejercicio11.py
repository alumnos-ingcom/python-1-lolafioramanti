################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Este test prueba una función que se encarga de analizar si un número entero es múltiplo de otro.
Se probará con valores positivos, negativos, neutros y cuando el múltiplo es mayor, menor o igual al número.
"""
import pytest

from src.ejercicio11 import es_multiplo

def test_es_multiplo_mayor():
    ''' multiplo > numero '''
    numero = -2
    multiplo = 12
    resultado = es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), "ERROR, el resultado debe ser un valor booleano"
    assert resultado == False, "ERROR, un número no puede tener como múltiplo a un número mayor que él"
    
def test_es_multiplo_menor():
    ''' multiplo < numero '''
    numero = -12
    multiplo = -2
    resultado = es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), "ERROR, el resultado debe ser un valor booleano"
    assert resultado == True, "ERROR, el resultado corresponde a 'True' "

def test_es_multiplo_igual():
    ''' multiplo = numero '''
    numero = 5
    multiplo = 5
    resultado = es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), "ERROR, el resultado debe ser un valor booleano"
    assert resultado == True, "ERROR, el resultado corresponde a 'True' "
    
def test_es_multiplo_cero():
    ''' multiplo = 0 '''
    numero = 2
    multiplo = 0
    resultado = es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), "ERROR, el resultado debe ser un valor booleano"
    assert resultado == False, "ERROR, un número no puede tener como múltiplo cero"
    
def test_es_multiplo_num_cero():
    ''' numero = 0 '''
    numero = 0
    multiplo = 8
    resultado = es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), "ERROR, el resultado debe ser un valor booleano"
    assert resultado == False, "ERROR, el cero no tiene múltiplos"