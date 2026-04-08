def transformar_en_cadena(texto, lista_pasos):
    resultado = texto
    for paso in lista_pasos:
        if paso == 1:
            resultado = resultado.upper()
        elif paso == 2:
            resultado = resultado.lower()
        elif paso == 3:
            resultado = resultado.capitalize()
    return resultado  # Solo devuelve el último estado
