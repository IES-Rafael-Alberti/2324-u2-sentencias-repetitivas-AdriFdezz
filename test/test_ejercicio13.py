from src.ejercicio13 import eco

def test_eco():
    assert eco("hola") == "Eco: hola"
    assert eco("salir") == "Terminado"