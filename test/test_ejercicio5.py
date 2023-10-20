from src.ejercicio5 import calcular_inversion

def test_calcular_inversion():
    resultado = calcular_inversion(1000, 5)
    assert resultado == 1050.00
