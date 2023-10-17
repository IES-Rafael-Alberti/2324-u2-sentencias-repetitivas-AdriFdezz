from src.ejercicio9 import verificar_contrasena

def test_verificar_contrasena():
    assert verificar_contrasena("hola123", "hola123") == True
    assert verificar_contrasena("contrasena", "hola123") == False