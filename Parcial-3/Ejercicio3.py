lecturas = []

for i in range(5):
    temperatura = int(input("Ingrese lectura de temperatura: "))
    lecturas.append(temperatura)

for t in lecturas:
    match t:
        case 0:
            print("Alerta: Punto de Congelación")
        case 100:
            print("Alerta: Punto de Ebullición")
        case _:
            estado = "Estado: Estable" if 10 <= t <= 30 else "Estado: Crítico"
            print(estado)