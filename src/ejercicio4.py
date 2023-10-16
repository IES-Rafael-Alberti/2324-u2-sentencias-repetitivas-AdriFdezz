#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
#la cuenta atrás desde ese número hasta cero separados por comas.

def cuenta_atras(numero):
    if numero >= 0:
        cuenta = ""
        for i in range(numero, -1, -1):
            cuenta += str(i)
            if i > 0:
                cuenta += ", "
        return "Cuenta atras desde " + str(numero) + " hasta 0: " + cuenta
    else:
        return "Escribe un numero entero positivo."

if __name__ == "__main__":
    numero = int(input("Escribe un numero entero positivo: "))
    resultado = cuenta_atras(numero)
    print(resultado)
