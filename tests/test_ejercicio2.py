################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Este test prueba la función signo, que se encarga de evaluar el signo de un número. 
Se probará como se comporta con números positivos, negativos y neutros.
"""
import pytest

from src.ejercicio2 import signo

def test_signo_positivo():
    '''
        Función con valores positivos.
    '''
    numero = 3
    valor = signo(numero)
    assert isinstance(valor, int), "El valor debe ser un número entero"
    assert valor == 1, "ERROR. No es el resultado esperado en cuanto a números POSITIVOS."
    
def test_signo_negativo():
    '''
        Función con valores negativos.
    '''
    numero = -3
    valor = signo(numero)
    assert isinstance(valor, int), "El valor debe ser un número entero"
    assert valor == -1, "ERROR. No es el resultado esperado en cuanto a números NEGATIVOS"

def test_signo_neutro():
    '''
        Función con valor neutro.
    '''
    numero = 0
    valor = signo(numero)
    assert isinstance(valor, int), "El valor debe ser un número entero"
    assert valor == 0, "ERROR. No es el resultado esperado en cuanto al número '0' "