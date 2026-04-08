def transformar_lista(lista, numero):
    nueva_lista = []

    for palabra in lista:
        if numero == 1:
            nueva_lista.append(palabra.upper())
        elif numero == 2:
            nueva_lista.append(palabra.lower())
        elif numero == 3:
            nueva_lista.append(palabra.capitalize())
        else:
            return "Opción no válida"

    return nueva_lista


palabrasATransformar = input("Ingrese varias palabras separadas por espacio: ")
listaDeUsuario = palabrasATransformar.split()
opcion = int(input("Elija una opción (1: Mayúsculas, 2: Minúsculas, 3: Capitalizar): "))


resultado_final = transformar_lista(listaDeUsuario, opcion)

# se imprime resultado final junto con la opción seleccionada y ademas incluyo el metodo join para que las palabras se muestren juntas y no en corchetes
print("Resultado Final:", " ".join(resultado_final), "- Opción seleccionada:", opcion)
