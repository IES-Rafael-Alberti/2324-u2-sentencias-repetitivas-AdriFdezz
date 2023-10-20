from src.ejercicio6 import triangulo_rectangulo

def test_triangulo_rectangulo():
    resultado = triangulo_rectangulo(5)
    assert resultado == "*\n**\n***\n****\n*****\n"