#Escribir un programa que pregunte al usuario una cantidad a invertir
#el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión 
#cada año que dura la inversión.

def calcular_inversion(cantidad, interes):
    capital = cantidad
    capital *= 1 + interes / 100
    return capital

if __name__ == "__main__":
    cantidad = float(input("Escribe la cantidad a invertir: "))
    interes = float(input("Escribe el interes anual en porcentaje: "))
    anios = int(input("Escribe el numero de años de la inversion: "))

    for anio in range(1, anios + 1):
        cantidad = calcular_inversion(cantidad, interes)
        print("Año " + str(anio) + " Capital obtenido = " + str("{:.2f}".format(cantidad)))

