def transformar_palabra(palabra, numero):
    # definino las funciones que se utilizaran

    if numero == 1:
        resultado = palabra.upper()
    elif numero == 2:
        resultado = palabra.lower()
    elif numero == 3:
        resultado = palabra.capitalize()
    else:
        resultado = "Opción no válida"

    print(resultado)


# ABAJO de la función pedimos los datos
palabra = input("Ingrese la palabra que desea transformar: ")
# agrege el int para que solo sean validos los numeros enteros
numero = int(input("Elija una opción (1: Mayúsculas, 2: Minúsculas, 3: Capitalizar: "))

# Llamamos a la función
transformar_palabra(palabra, numero)
