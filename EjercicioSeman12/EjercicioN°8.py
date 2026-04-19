triangulo1 = int(input("Ingrese la medida de un triángulo: "))
triangulo2 = int(input("Ingrese la medida del otro lado del triángulo: "))
triangulo3 = int(input("Ingrese la medida del tercer lado del triángulo: "))


def tipo_triangulo(triangulo1, triangulo2, triangulo3):
    if triangulo1 == triangulo2 == triangulo3:
        print("El triángulo es equilátero.")
    elif (
        triangulo1 == triangulo2 or triangulo1 == triangulo3 or triangulo2 == triangulo3
    ):
        print("El triángulo es isósceles.")
    else:
        print("El triángulo es escaleno.")


tipo_triangulo(triangulo1, triangulo2, triangulo3)
