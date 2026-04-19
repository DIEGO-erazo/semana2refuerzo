monto = int(input("Ingrese el monto de la compra: "))


def calcular_descuento(monto):
    if monto >= 100:
        descuento = "20%"
    elif 50 < monto < 100:
        descuento = "10%"
    elif monto < 50:
        descuento = "0%"
    return descuento


print("El descuento aplicado es: ", calcular_descuento(monto))
calcular_descuento(monto)
