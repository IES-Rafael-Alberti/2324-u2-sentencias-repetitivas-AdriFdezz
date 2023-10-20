from src.ejercicio24 import numeros_primos


def test_numeros_primos():
    assert numeros_primos(2) == True
    assert numeros_primos(4) == False