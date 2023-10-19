from src.ejercicio16 import numero_mayor

def test_numero_mayor():
    numeros = [5, 3, 10, 17]
    resultado = numero_mayor(numeros)
    assert resultado == 17