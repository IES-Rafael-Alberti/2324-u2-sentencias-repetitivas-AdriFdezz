#Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). 
#Recorrer la frase, carácter a carácter, comparando con la letra buscada. 
#Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. 
#Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.

def buscar_letra(frase, letra):
    for posicion, caracter in enumerate(frase):
        if caracter == letra:
            return posicion
    return -1

if __name__ == "__main__":
    frase = input("Escribe una frase: ")
    letra = input("Escribe una letra: ")

    posicion = buscar_letra(frase, letra)

    if posicion != -1:
        resultado = "La letra '" + letra + "' se encuentra en la posicion " + str(posicion) + " de la frase: '" + frase
    else:
        resultado = "No se encontro la letra '" + letra + "' en la frase: '" + frase

    print(resultado)
