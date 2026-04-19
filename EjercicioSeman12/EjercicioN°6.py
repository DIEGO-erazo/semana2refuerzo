diaSemana = int(
    input("Ingrese un número del 1 al 7 para conocer el día de la semana: ")
)


def dia_de_la_semana(diaSemana):
    if diaSemana == 1:
        print("El día de la semana es lunes.")
    elif diaSemana == 2:
        print("El día de la semana es martes.")
    elif diaSemana == 3:
        print("El día de la semana es miércoles.")
    elif diaSemana == 4:
        print("El día de la semana es jueves.")
    elif diaSemana == 5:
        print("El día de la semana es viernes.")
    elif diaSemana == 6:
        print("El día de la semana es sábado.")
    elif diaSemana == 7:
        print("El día de la semana es domingo.")
    else:
        print("Número no válido. Por favor ingrese un número del 1 al 7.")


dia_de_la_semana(diaSemana)
