edad = int(input("Ingrese su edad: "))


def es_mayor_de_edad(edad):
    if edad >= 18 and edad < 60:
        print("Eres mayor de edad.")
    elif edad >= 60:
        print("Eres un adulto mayor.")
    else:
        print("Eres menor de edad.")


es_mayor_de_edad(edad)
