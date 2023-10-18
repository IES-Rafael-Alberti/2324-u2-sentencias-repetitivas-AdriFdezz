#Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
#Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

def sumar_numeros_positivos(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

if __name__ == "__main__":
    numeros = []
    numero = int(input("Escribe un numero o 0 para terminar: "))
    
    while numero != 0:
        if numero > 0:
            numeros.append(numero)
        numero = int(input("Escribe otro numero o 0 para terminar: "))
    
    resultado = sumar_numeros_positivos(numeros)
    print("La suma de los numeros positivos ingresados es:", resultado)