Algoritmo DivisionContinua
    // Definimos las variables de forma sencilla
    Definir n Como Real
    Definir terminar Como Logico
    
    // Inicializamos
    terminar <- Falso
    
    Escribir "Ingresa un numero para dividir:"
    Leer n
    
    // Estructura Hacer-Mientras (Repetir)
    Repetir
        n <- n / 2
        Escribir "Resultado: ", n
        
        // Verificamos si ya es menor a 1
        Si n < 1 Entonces
            terminar <- Verdadero
        FinSi
        
    Hasta Que terminar = Verdadero
    
    Escribir "Terminado, el numero es menor a 1 ."
FinAlgoritmo