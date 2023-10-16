#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def repetir_palabra(palabra):
    palabra_repetida = ""
    for i in range(10):
        palabra_repetida += palabra + " "
    return palabra_repetida

if __name__ == "__main__":
    palabra = input("Escribe una palabra: ")
    resultado = repetir_palabra(palabra)
    print(resultado)