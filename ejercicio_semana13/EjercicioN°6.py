while True:
    n = int(input("Ingresa n (0 para salir): "))
    if n == 0:
        break
    for i in range(1, n + 1):
        if i > 1:
            es_primo = True
            for j in range(2, i):
                if i % j == 0:
                    es_primo = False
                    break
            if es_primo:
                print(i)
