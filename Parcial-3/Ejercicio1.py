etiqueta = input("Ingrese la etiqueta de rastreo: ")

if not etiqueta:
    print("Error: La entrada está vacía.")
else:
    categoria = etiqueta[5:-3]
    print(categoria)

    ruta = "Ruta Local" if etiqueta.endswith("SV") else "Ruta Internacional"
    print(ruta)