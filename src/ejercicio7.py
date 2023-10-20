#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

def tabla_de_multiplicar():
    tabla = ""
    for tablas in range(1, 11):
        for tablas2 in range(1, 11):
            resultado = tablas * tablas2
            tabla += str(tablas) + " x " + str(tablas2) + " = " + str(resultado) + "\n"
        tabla += "\n"
    return tabla

if __name__ == "__main__":
    tabla = tabla_de_multiplicar()
    print(tabla)

