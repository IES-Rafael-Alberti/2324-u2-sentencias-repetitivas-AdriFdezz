#Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga 
#(en caso de haber más de una, mostrar la primera) y cuántas palabras había. 
#Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.

def palabra_larga(frase):
    palabras = frase.split()
    palabra_mas_larga = ""
    for palabra in palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    cantidad_palabras = len(palabras)
    return palabra_mas_larga, cantidad_palabras

if __name__ == "__main__":
    frase = input("Escribe una frase: ")
    
    palabra_mas_larga, cantidad_palabras = palabra_larga(frase)

    if cantidad_palabras > 0:
        print("La palabra mas larga es: " + palabra_mas_larga)
        print("Cantidad de palabras en la frase: " + str(cantidad_palabras))
