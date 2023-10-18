#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla 
#el número de veces que aparece la letra en la frase.

def contador_letra(frase, letra):
    contador = 0
    for caracter in frase:
        if caracter == letra:
            contador += 1
    return contador

if __name__ == "__main__":
    frase = input("Escribe una frase: ")
    letra = input("Escribe una letra: ")

    if len(letra) == 1:
        cantidad = contador_letra(frase, letra)
        print("La letra " + letra + " aparece " + str(cantidad) + " veces en la frase")
    else:
        print("Escribe una sola letra")
