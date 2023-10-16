#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido 
#(desde 1 hasta su edad).

def cumplidos(edad):
    if edad < 0:
        return "No puede ser negativa."
    
    return list(range(1, edad + 1))

if __name__ == "__main__":
    edad = int(input("Escribe tu edad: "))
    anios_cumplidos = cumplidos(edad)

    if type(anios_cumplidos) == list:
        print("Años cumplidos:")
        for anio in anios_cumplidos:
            print(anio)
    else:
        print(anios_cumplidos)
