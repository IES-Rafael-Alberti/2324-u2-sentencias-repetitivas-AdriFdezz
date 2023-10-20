#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo 
#como el de más abajo, de altura el número introducido.

#*
#**
#***
#****
#*****

def triangulo_rectangulo(altura):
    triangulo = ""
    for i in range(1, altura + 1):
        for j in range(i):
            triangulo += "*"
        triangulo += "\n"
    return triangulo

if __name__ == "__main__":
    altura = int(input("Escribe un numero entero para la altura del triangulo: "))
    triangulo = triangulo_rectangulo(altura)
    print(triangulo)
