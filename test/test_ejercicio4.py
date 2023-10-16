from src.ejercicio4 import cuenta_atras

def test_cuenta_atras():
    assert cuenta_atras(5) == "Cuenta atras desde 5 hasta 0: 5, 4, 3, 2, 1, 0"
    assert cuenta_atras(-5) == "Escribe un numero entero positivo."