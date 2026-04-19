Num1 = int(input("Ingrese un numero a operar: "))
Num2 = int(input("Ingrese otro numero a operar: "))
Operacion = input("Ingrese la operacion matematica a realizar (+, -, *, /): ")


def calculadora(n1, n2, operacion):
    if operacion == "+":
        return n1 + n2
    elif operacion == "-":
        return n1 - n2
    elif operacion == "*":
        return n1 * n2
    elif operacion == "/":
        if n2 != 0:
            return n1 / n2
        else:
            return "Error: No se puede dividir entre cero"
    else:
        return "Operación no válida"


# --- Llamamos a la función solo una vez ---
resultado = calculadora(Num1, Num2, Operacion)

# --- Mostramos el resultado ---
print("El resultado de la operacion es:", resultado)
