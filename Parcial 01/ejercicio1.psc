Algoritmo CalificacionEstudiante
    Definir nota Como Real
    Escribir "Ingrese la nota del estudiante (0 a 10):"
    Leer nota
    Si nota >= 6 Entonces
        Escribir "Aprobado"
    Sino
        Si nota <= 4 Entonces
            Escribir "Reprobado"
        Sino
            Escribir "Recuperación"
        FinSi
    FinSi
FinAlgoritmo