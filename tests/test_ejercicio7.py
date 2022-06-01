################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Este test prueba funciones que convierten valores sexadecimales en decimales (y viceversa).
Se probarán valores enteros (se descartan valores negativos, o mayores a 60 por las restricciones de la función principal.
"""

import pytest

from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal
    
def test_sexadecimal_a_decimal():
    horas = 1
    minutos = 2
    segundos = 3
    resultado = sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(resultado, tuple), "ERROR, el resultado debe ser del tipo tuple"
    assert resultado == (3723,), "ERROR, el resultado debe ser 3723s"
    assert minutos < 60, "ERROR, los minutos deben estar entre 0 y 59"
    assert minutos >= 0, "ERROR, los minutos no pueden ser negativos"
    assert segundos < 60, "ERROR, los segundos deben estar entre 0 y 59"
    assert segundos >= 0, "ERROR, los segundos no pueden ser negativos"
    
def test_decimal_a_sexadecimal():
    segundos = 456
    resultado = decimal_a_sexadecimal(segundos)
    assert isinstance(resultado, tuple), "ERROR, el resultado debe ser del tipo tuple"
    assert resultado == (0, 7, 36), "ERROR, el resultado debe ser 0hs 7min 36s"
    assert segundos >= 0, "ERROR, los segundos no pueden ser negativos"
    
    
    