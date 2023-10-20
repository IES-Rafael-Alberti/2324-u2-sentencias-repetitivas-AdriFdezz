#Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. 
#Por cada número, informar cuántos dígitos pares y cuántos impares tiene. 
#Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.

def contar_pares_impares(numero):
    digitos_pares = 0
    digitos_impares = 0

    while numero > 0:
        digito = numero % 10

        if digito % 2 == 0:
            digitos_pares += 1
        else:
            digitos_impares += 1

        numero //= 10

    return digitos_pares, digitos_impares

if __name__ == "__main__":
    total_digitos_pares = 0
    total_digitos_impares = 0
    numero = int(input("Introduce un numero entero positivo 0 para finalizar: "))

    while numero != 0:
        if numero < 0:
            print("El numero ingresado no es positivo")
        else:
            digitos_pares, digitos_impares = contar_pares_impares(numero)
            total_digitos_pares += digitos_pares
            total_digitos_impares += digitos_impares
            print("El numero", numero, "tiene", digitos_pares, "digitos pares y", digitos_impares, "digitos impares.")
        
        numero = int(input("Introduce un numero entero positivo 0 para finalizar: "))

    print("Total de digitos pares:", total_digitos_pares)
    print("Total de digitos impares:", total_digitos_impares)
