def validar_opcion(texto, numero):
    # La prioridad es detectar si el número NO es 1, 2 o 3
    if numero == 1 or numero == 2 or numero == 3:
        # Aquí podrías poner la transformación, pero el ejercicio
        # se enfoca en que si el número es válido, el programa continúa.
        print("Opción válida para el texto:", texto)
    else:
        # Esto es lo que pide el ejercicio 5 específicamente
        print("opción inválida")


# --- Entrada de datos ---
texto_usuario = input("Ingrese un texto: ")
opcion_usuario = int(input("Ingrese un número (1, 2 o 3): "))

# Llamamos a la función para validar
validar_opcion(texto_usuario, opcion_usuario)
