def transformar_palabra(palabra, numero):
    if numero == 1:
        return palabra.upper()
    elif numero == 2:
        return palabra.lower()
    elif numero == 3:
        return palabra.capitalize()

    else:
        return "Opción no válida : " + palabra


palabra = input("Palabra: ")
numero = int(
    input("Elija una opción (1: Mayúsculas, 2: Minúsculas, 3: Capitalizar):  ")
)
resultado = transformar_palabra(palabra, numero)
print(resultado)
