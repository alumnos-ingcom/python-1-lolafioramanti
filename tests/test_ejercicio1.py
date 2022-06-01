################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Este test prueba las funciones de conversión de grados. 
Se probará como se comporta con números enteros, con parte fraccionaria, negativos y positivos.
"""

import pytest

from src.ejercicio1 import convertir_a_fahrenheit, convertir_a_centigrados

def test_convertir_a_fahrenheit_positivo():
    """
       Test con valores positivos en la función que convierte de centígrados a fahrenheit.
    """
    centigrados = 12
    resultado = convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado debe ser un número con parte fraccionaria"
    assert resultado == 53.6, "No se obtuvo el resultado esperado conviertiendo números POSITIVOS ENTEROS de Cº a Fº"
    
def test_convertir_a_fahrenheit_positivo_coma():
    """
       Test con valores positivos con parte fraccionaria en la función que convierte de centígrados a fahrenheit.
    """
    centigrados = 2.5
    resultado = convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado debe ser un número con parte fraccionaria"
    assert resultado == 36.5, "No se obtuvo el resultado esperado convirtiendo números POSITIVOS CON PARTE FRACCIONARIA de Cº a Fº"
    
def test_convertir_a_fahrenheit_negativo():
    '''
        Test con valores negativos en la función que convierte de centígrados a fahrenheit.
    '''
    centigrados = -3
    resultado = convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado debe ser un número con parte fraccionaria"
    assert resultado == 26.6, "No se obtuvo el resultado esperado convirtiendo números NEGATIVOS de Cº a Fº"
    
def test_convertir_a_fahrenheit_negativo_coma():
    '''
        Test con valores negativos con parte fraccionaria en la función que convierte de centígrados a fahrenheit.
    '''
    centigrados = -17.5
    resultado = convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado debe ser un número con parte fraccionaria"
    assert resultado == 0.5, "No se obtuvo el resultado esperado convirtiendo números NEGATIVOS CON PARTE FRACCIONARIA de Cº a Fº"
    
def test_convertir_a_centigrados_positivo():
    '''
        Test con valores positivos en la función que convierte de fahrenheit a centígrados.
    '''
    fahrenheit = 23
    resultado = convertir_a_centigrados(fahrenheit)
    assert isinstance(resultado, float), "El resultado debe ser un número con parte fraccionaria"
    assert resultado == -5.0, "No se obtuvo el resultado esperado convirtiendo números POSITIVOS de Fº a Cº"
    
def test_convertir_a_centigrados_positivo_coma():
    '''
        Test con valores positivos con parte fraccionaria en la función que convierte de fahrenheit a centígrados.
    '''
    fahrenheit = 3.2
    resultado = convertir_a_centigrados(fahrenheit)
    assert isinstance(resultado, float), "El resultado debe ser un número con parte fraccionaria"
    assert resultado == -16.0, "No se obtuvo el resultado esperado convirtiendo números POSITIVOS CON PARTE FRACCIONARIA de Fº a Cº"
    
def test_convertir_a_centigrados_negativo():
    '''
        Test con valores negativos en la función que convierte de fahrenheit a centígrados"
    '''
    fahrenheit = -4
    resultado = convertir_a_centigrados(fahrenheit)
    assert isinstance(resultado, float), "El resultado debe ser un número con parte fraccionaria"
    assert resultado == -20.0, "No se obtuvo el resultado esperado convirtiendo números NEGATIVOS de Fº a Cº"
    
def test_convertir_a_centigrados_negativo_coma():
    '''
        Test con valores negativos con parte fraccionaria en la función que convierte de fahrenheit a centígrados"
    '''
    fahrenheit = -2.2
    resultado = convertir_a_centigrados(fahrenheit)
    assert isinstance(resultado, float), "El resultado debe ser un número con parte fraccionaria"
    assert resultado == -19.0, "No se obtuvo el resultado esperado convirtiendo números NEGATIVOS CON PARTE FRACCIONARIA de Fº a Cº"