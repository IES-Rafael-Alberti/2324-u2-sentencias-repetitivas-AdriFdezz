#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. 
#Informar cuál fue el mayor número ingresado.

def numero_mayor(numeros):
    mayor = 0
    for numero in numeros:
        if numero > mayor:
            mayor = numero
    return mayor

if __name__ == "__main__":
    numeros = []
    numero = int(input("Escribe un numero entero positivo o 0 para terminar: "))

    while numero != 0:
        if numero > 0:
            numeros.append(numero)
        numero = int(input("Escribe otro numero entero positivo o 0 para terminar: "))

    if not numeros:
        print("No se ingresaron numeros positivos")
    else:
        mayor = numero_mayor(numeros)
        print("El mayor numero ingresado es: " + str(mayor))
