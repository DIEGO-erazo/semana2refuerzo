Nota = int(input("Ingrese su nota: "))


def evaluar_nota(Nota):
    if Nota >= 9 and Nota <= 10:
        print("Excelente")
    elif Nota >= 7 and Nota <= 8:
        print("Bueno")
    elif Nota == 6:
        print("Aprobado")
    elif Nota >= 0 and Nota <= 5:
        print("Reprovado")
    else:
        print("Nota inválida. Por favor ingrese una nota entre 0 y 10.")


evaluar_nota(Nota)
