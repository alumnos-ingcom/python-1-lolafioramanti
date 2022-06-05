################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Este test prueba funciones que en conjunto buscan el cociente y resto de dos números.
Se probará como se comportan los programas ingresando números negativos, positivos, y mayores, menores o iguales entre entradas.
"""

import pytest

from src.ejercicio5 import valor_absoluto, division_lenta

def test_valor_absoluto_n_n():
    '''
        el dividendo y divisor son negativos.
    '''
    dividendo = -12
    divisor = -3
    