#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

def primo(numero):
    if numero <= 1:
        return "no es primo"
    if numero <= 3:
        return "es primo"
    if numero % 2 == 0 or numero % 3 == 0:
        return "no es primo"
    verificador = 5
    while verificador * verificador <= numero:
        if numero % verificador == 0 or numero % (verificador + 2) == 0:
            return "no es primo"
        verificador += 6
    return "es primo"

if __name__ == "__main__":
    numero = int(input("Escribe un numero entero: "))
    resultado = primo(numero)
    print(str(numero) + " " + resultado)

