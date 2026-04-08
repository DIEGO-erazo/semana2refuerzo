##cree el menu lo mas legible posible para que sea facil para que el usuario y adems agree una broma
def mostrar_menu():
    print("\n--- MENÚ DE TRANSFORMACIÓN ---")
    print("1. Convertir a Mayúsculas")
    print("2. Convertir a Minúsculas")
    print("3. Capitalizar (Primera letra Mayúscula)")
    print("4. Verás a lo que todo Ing. en Sistemas le tiene miedo")
    print("-" * 30)


def ejecutar_programa():
    # 1. Pedimos el texto a transformar
    texto = input("Ingrese el texto a transformar: ")

    mostrar_menu()

    # Capturamos la opción
    opcion = int(input("Seleccione una opción (1-4): "))

    # Variable para el mensaje único
    resultado = ""

    if opcion == 1:
        texto = texto.upper()
        resultado = "Resultado actual: " + texto
    elif opcion == 2:
        texto = texto.lower()
        resultado = "Resultado actual: " + texto
    elif opcion == 3:
        texto = texto.capitalize()
        resultado = "Resultado actual: " + texto
    elif opcion == 4:
        # Aquí agrege a lo que todo ign en sistmas le tiene miedo , una pala :)
        pala = """
             _________________
            |                |
            |    CUIDADO...  |
            |    UNA PALA!   |
            |________________|
                   |  |
                   |  |
                   |  |
                  /    \\
                 /______\\
        """
        resultado = (
            pala + "\nSaliendo del programa... ¡Huye antes de que te pongan a trabajar!"
        )
    else:
        resultado = "Opción inválida"

    # UN SOLO PRINT que muestra todo (incluida la pala si eliges 4)
    print(resultado)


# Iniciamos el programa
ejecutar_programa()
