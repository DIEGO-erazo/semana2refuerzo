nombre_completo = input("Ingrese nombre y apellido completo: ")
palabras = nombre_completo.split()
lista_invertida = palabras[::-1]

for palabra in lista_invertida:
    palabra_puntos = ""
    for i in range(len(palabra)):
        palabra_puntos += palabra[i]
        if i < len(palabra) - 1:
            palabra_puntos += "."
    print(palabra_puntos)