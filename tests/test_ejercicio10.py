

import pytest

from src.ejercicio10 import es_palindromo

def test_es_palindromo_espacios():
    ''' El texto tiene espacios. '''
    texto = "yo hago yoga hoy"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "ERROR, el resultado debe ser un valor booleano"
    assert resultado == True, "ERROR, esta frase corresponde a 'True' "
    
def test_es_palindromo_palabra():
    ''' EL texto tiene sólo una palabra (carece de espacios). '''
    texto = "radar"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "ERROR, el resultado debe ser un valor booleano"
    assert resultado == True, "ERROR, esta frase corresponde a 'True' "
    
def test_es_palindromo_mayuscula():
    ''' El texto tiene letras mayúsculas y minúsculas. '''
    texto = "Anita lava la tina"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "ERROR, el resultado debe ser un valor booleano"
    assert resultado == True, "ERROR, esta frase corresponde a 'True' "
    
def test_es_palindromo_tilde():
    ''' El texto tiene tildes. '''
    texto = "ananá"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "ERROR, el resultado debe ser un valor booleano"
    assert resultado == False, "ERROR, esta frase corresponde a 'False' "
    