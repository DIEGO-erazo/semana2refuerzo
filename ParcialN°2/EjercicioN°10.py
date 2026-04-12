Lenguaje = "Python2026"
resultado1 = Lenguaje.isalnum()
print("¿Es alfanumérico?:", resultado1)


if resultado1 == True:
    texto_minusc = Lenguaje.lower()

    solo_palabra = texto_minusc.replace("2026", "")
    print("Rsultado Final :", solo_palabra)
