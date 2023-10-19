#Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa.
#A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). 
#Si elige una opción incorrecta, informarle del error. 
#El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. 
#Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, 
#se interrumpirá la impresión del menú y el programa finalizará.

def menu(opcion):
    opciones_validas = {"1", "2", "3"}
    if opcion in opciones_validas:
        return opcion
    else:
        return "Opcion incorrecta. Seleccione 1, 2 o 3"

if __name__ == "__main__":
    programa_activo = True

    while programa_activo:
        print("Menu:\n1 - Comenzar programa\n2 - Imprimir listado\n3 - Finalizar programa")
        opcion = menu(input("Elija una opción (1/2/3): "))

        if opcion == "1":
            print("Ha seleccionado comenzar programa")
        elif opcion == "2":
            print("Ha seleccionado imprimir listado")
        elif opcion == "3":
            print("Ha seleccionado finalizar programa. Saliendo del programa")
            programa_activo = False
        else:
            print(opcion)
