Archivo = "Diego.txt"
paso1 = Archivo.removesuffix(".txt")
paso2 = paso1.removeprefix("ING. ")

resultado_limpio = paso2.lower()
resultado_final = resultado_limpio.split()

print("Texto en minúsculas:", resultado_limpio)
print("Resultado final es :", (resultado_final))
