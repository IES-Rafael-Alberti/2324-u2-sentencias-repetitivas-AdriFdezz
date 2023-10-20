from src.ejercicio10 import primo

def test_primo():
    assert primo(1) == "no es primo"
    assert primo(2) == "es primo"