while True:
    n = int(input("Nivel del triángulo (0 para salir): "))
    if n == 0:
        break
    for i in range(1, n + 1):
        if i % 2 != 0:
            print("*" * i)
