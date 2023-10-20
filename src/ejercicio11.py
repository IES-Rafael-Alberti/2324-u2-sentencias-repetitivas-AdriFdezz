#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra 
#introducida empezando por la última.

def palabra_inversa(palabra):
    inversa = []
    for letra in reversed(palabra):
        inversa.append(letra)
    return inversa

if __name__ == "__main__":
    palabra = input("Escribe una palabra: ")
    inversa = palabra_inversa(palabra)
    print("Palabra en orden inverso:")
    for letra in inversa:
        print(letra)
