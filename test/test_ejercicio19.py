from src.ejercicio19 import menu

def test_obtener_opcion():
    assert menu("1") == "1"
    assert menu("2") == "2"
    assert menu("3") == "3"
    assert menu("4") == "Opcion incorrecta. Seleccione 1, 2 o 3"