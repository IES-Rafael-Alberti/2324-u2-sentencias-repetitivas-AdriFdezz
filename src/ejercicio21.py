#Crear un programa que permita al usuario ingresar los montos de las compras de un cliente 
#(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso 
#de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y se debe pedir 
#que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas 
#superan el total de $1000, se le debe aplicar un 10% de descuento.

def calcular_compra(compras):
    total = sum(compras)
    if total > 1000:
        total -= total * 0.10
    return total

if __name__ == "__main__":
    montos_compra = []  
    monto = float(input("Introduce el monto de la compra (0 para finalizar): "))
    
    while monto != 0:
        if monto < 0:
            print("El monto no puede ser negativo. Ingrese un nuevo monto.")
        else:
            montos_compra.append(monto)
        monto = float(input("Introduce el monto de la compra (0 para finalizar): "))

    total_a_pagar = calcular_compra(montos_compra)

    print("Montos de compra:", montos_compra)
    print("El total a pagar es:", total_a_pagar)

