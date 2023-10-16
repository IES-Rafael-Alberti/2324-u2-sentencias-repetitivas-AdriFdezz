from src.ejercicio2 import cumplidos

def test_cumplidos():
    assert cumplidos(5) == [1, 2, 3, 4, 5]
    assert cumplidos(-5) == "No puede ser negativa."