#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

def eco(entrada):
    if entrada.lower() == "salir":
        return "Terminado"
    else:
        return "Eco: " + entrada

if __name__ == "__main__":
    entrada = input("Escribe algo o escribe salir para terminar: ")
    
    while entrada.lower() != "salir":
        resultado = eco(entrada)
        print(resultado)
        entrada = input("Escribe algo o escribe salir para terminar: ")
