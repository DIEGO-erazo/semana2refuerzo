impares = []
suma = 0
while True:
    num = int(input("Ingresa un número (0 para salir): "))
    if num == 0:
        break
    if num % 2 != 0:
        suma += num
        impares.append(num)

print(f"Suma total: {suma}")
for n in impares:
    print(f"Impar ingresado: {n}")
