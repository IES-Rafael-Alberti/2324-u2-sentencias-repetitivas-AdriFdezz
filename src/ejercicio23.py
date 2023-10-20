#Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso 
#al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 
#que contenga sólo una barra (“/”) se considera que termina una línea. 
#Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) 
#aparecieron en total (en todos los títulos de libros que componen en esa línea). Finalmente, informar 
#cuántas líneas completas se ingresaron.

def contar_digitos(linea):
    digitos = 0
    for caracter in linea:
        if caracter >= '0' and caracter <= '9':
            digitos += 1
    return digitos

if __name__ == "__main__":
    lineas_completas = 0
    titulo = ""
    linea_actual = ""

    while titulo != "*":
        titulo = input("Libro: ")

        if titulo == "/":
            if linea_actual:
                digitos = contar_digitos(linea_actual)
                print("Linea completa. Aparecen", digitos, "digitos numericos")
                lineas_completas += 1
            linea_actual = ""
        elif titulo != "*":
            linea_actual += titulo

    print("Fin. Se leyeron", lineas_completas, "lineas completas")
