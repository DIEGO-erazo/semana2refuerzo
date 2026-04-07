def transformar(texto, numero):
    if numero == 1:
        return texto.upper()
    elif numero == 2:
        return texto.lower()
    elif numero == 3:
        return texto.capitalize()
    else:
        return "Opción inválida"


frase = input("Frase: ")
opcion = int(input("Opción (1,2,3): "))
print(transformar(frase, opcion))
