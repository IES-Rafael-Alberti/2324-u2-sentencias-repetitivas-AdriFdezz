from src.ejercicio25 import palabra_larga

def test_palabra_larga():
    resultado = palabra_larga("Esto es una frase de prueba")
    assert resultado == ("prueba", 6)