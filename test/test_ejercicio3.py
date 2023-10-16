from src.ejercicio3 import numeros_impares

def test_numeros_impares():
    assert numeros_impares(10) == "1, 3, 5, 7, 9"
    assert numeros_impares(-5) == "Debes escribir un numero entero positivo."