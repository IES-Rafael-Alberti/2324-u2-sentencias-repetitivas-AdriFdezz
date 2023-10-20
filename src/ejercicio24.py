#Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
#finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.

def numeros_primos(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True

    if numero % 2 == 0 or numero % 3 == 0:
        return False

    divisor = 5
    while divisor * divisor <= numero:
        if numero % divisor == 0 or numero % (divisor + 2) == 0:
            return False
        divisor += 6

    return True

if __name__ == "__main__":
    cantidad_primos = 0
    numero = int(input("Introduce un numero mayor que 1 o 0 para finalizar: "))

    while numero != 0:
        if numero > 1 and numeros_primos(numero):
            cantidad_primos += 1
        numero = int(input("Introduce un numero mayor que 1 o 0 para finalizar: "))

    print("La cantidad de numeros primos introducidos es:", cantidad_primos)
