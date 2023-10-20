from src.ejercicio8 import triangulo_rectangulo_numeros

def test_triangulo_rectangulo_numeros():
    resultado = triangulo_rectangulo_numeros(5)
    referencia = "1 \n3 1 \n5 3 1 \n7 5 3 1 \n9 7 5 3 1 \n"
    assert resultado == referencia