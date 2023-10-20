#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por 
#la contraseña hasta que introduzca la contraseña correcta.

def verificar_contrasena(contrasena_ingresada, contrasena_correcta):
    if contrasena_ingresada == contrasena_correcta:
        return True
    else:
        return False

if __name__ == "__main__":
    contrasena_correcta = "hola123"
    contrasena_ingresada = input("Escribe la contraseña: ")
    
    while not verificar_contrasena(contrasena_ingresada, contrasena_correcta):
        print("Contraseña incorrecta")
        contrasena_ingresada = input("Escribe la contraseña: ")
    
    print("Acceso permitido.")