#Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.

def suma_digitos(numero):
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma

if __name__ == "__main__":
    numero = int(input("Escribe un numero entero positivo: "))
    if numero < 0:
        print("El numero debe ser positivo.")
    else:
        resultado = suma_digitos(numero)
        print("La suma de los digitos del numero " + str(numero) + " es: " + str(resultado))