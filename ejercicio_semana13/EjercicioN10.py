numeros = []
suma = 0
while suma <= 100:
    n = int(input("Ingresa un número: "))
    if n >= 0:
        suma += n
        numeros.append(n)
    if n < 0:
        print("Ignorado")

for n in numeros:
    print(f"Número válido: {n}")
