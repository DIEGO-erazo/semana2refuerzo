voz = "CANTANDO"

vozminuscula = voz.lower()
print(vozminuscula)

vozSInsuffix = vozminuscula.removesuffix("ando")
print(vozSInsuffix)

resultado = vozSInsuffix.find("t")
print(resultado)
