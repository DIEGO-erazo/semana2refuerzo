notas = []
while True:
    n = float(input("Nota (-1 para terminar): "))
    if n == -1:
        break
    if n >= 0 and n <= 10:
        notas.append(n)

suma = 0
for nota in notas:
    suma += nota

if len(notas) > 0:
    print(f"Promedio: {suma / len(notas)}")
