from decimal import Decimal

total = Decimal('0.00')

while True:
    entrada = input("Ingrese el precio del producto: ")
    if entrada == "0":
        break
    try:
        total += Decimal(entrada)
    except ValueError:
        print("Advertencia: Entrada inválida, el cobro continúa.")

print(f"Total acumulado de la compra: ${total}")