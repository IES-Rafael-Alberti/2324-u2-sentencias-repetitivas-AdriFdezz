#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
#todos los números impares desde 1 hasta ese número separados por comas.

def numeros_impares(numero):
    if numero > 0:
        numeros_impares = [str(i) for i in range(1, numero + 1) if i % 2 != 0]
        resultado = ", ".join(numeros_impares)
        return resultado
    else:
        return "Debes escribir un numero entero positivo."

if __name__ == "__main__":
    numero = int(input("EScribe un numero entero positivo: "))
    resultado = numeros_impares(numero)
    print(resultado)
