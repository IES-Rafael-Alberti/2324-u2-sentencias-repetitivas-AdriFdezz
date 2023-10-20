#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo 
#como el de más abajo

#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1

def triangulo_rectangulo_numeros(altura):
    triangulo = ""
    for numeros in range(1, altura * 2, 2):
        for numeros2 in range(numeros, 0, -2):
            triangulo += str(numeros2) + ' '
        triangulo += '\n'
    return triangulo

if __name__ == "__main__":
    altura = int(input("Escribe un numero entero para la altura del triangulo: "))
    resultado = triangulo_rectangulo_numeros(altura)
    print(resultado)
