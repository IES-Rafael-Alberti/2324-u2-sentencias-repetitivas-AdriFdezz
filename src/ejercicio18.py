#Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos 
#que lo componen. La condición de corte es que se ingrese el número -1. 
#Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.

def suma_digitos2(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma

if __name__ == "__main__":
    numeros_pares = 0
    contador_numeros = 0

    numero = int(input("Escribe un numero entero positivo -1 para salir: "))
    while numero != -1:
        suma = suma_digitos2(numero)
        print("La suma de los digitos es: " + str(suma))

        if numero % 2 == 0:
            numeros_pares += 1

        contador_numeros += 1
        numero = int(input("Escribe un numero entero positivo -1 para salir: "))

    print("Cantidad de numeros pares ingresados: " + str(numeros_pares))
    print("Cantidad total de numeros ingresados: " + str(contador_numeros))
