def transformar_palabra(palabra, numero):
    if numero == 1:
        return palabra.upper()
    elif numero == 2:
        return palabra.lower()
    elif numero == 3:
        return palabra.capitalize()

    else:
        return None


palabra = input("ingres una frase : ")
numero = int(
    input("Elija una opción (1: Mayúsculas, 2: Minúsculas, 3: Capitalizar):  ")
)
resultado1 = transformar_palabra(palabra, numero)

print(resultado1)

# Agrege esta validación para evitar errores si la opción es inválida
if resultado1 is not None:
    resultado2 = resultado1.replace(" ", "")
    print("caracteres sin contar los espacios", len(resultado2))
else:
    print("No se pudo realizar el conteo porque la opción es inválida.")
