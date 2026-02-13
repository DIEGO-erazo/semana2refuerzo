Algoritmo Ejemplo2
	Definir cajero, cuentaDeAhorro, numeroCuenta, cantidadSaliente, Saldo, preguntar Como Entero
	cuentaDeAhorro <- 1000
	numeroDeCuenta <- 12345
	Escribir ' bienvenido'
	Escribir ' Actividad que desea realizar'
	Escribir ' 1 para consultar'
	Escribir ' 2 para extraer dinero de la cuenta  de ahorro'
	Escribir ' Escriba el nunero de cuenta a operar'
	Leer preguntar
	Si preguntar==1 Entonces
		Escribir ' Escriba el nunero de cuenta a operar' // yo no quiero ser un uno mejor busco otra chamba
		Leer preguntar
		Si preguntar==numeroDeCuenta Entonces
			Escribir 'Su saldo es ', cuentaDeAhorro // es valor den numero de cuentas
		FinSi
	FinSi
	Si preguntar==2 Entonces
		Escribir ' Escriba el nunero de cuenta a operar'
		Leer preguntar
		Si preguntar==numeroDeCuenta Entonces
			Escribir ' Escriba el monto a extraer' // es valor den numero de cuentas
			Leer preguntar
			// < =
			Si preguntar<=cuentaDeAhorro Entonces
				Saldo <- cuentaDeAhorro-preguntar // es la cantidad a extraer
				Escribir 'Procesando'
				Escribir 'Su saldo actual es de ', Saldo
			FinSi
		FinSi
	FinSi
	// or  o pues llevar
	// panes con cafe o chocolate
	// and  puedes llevar carne y jamon
	// not mejor no
	// == si es igual
	// <>  diferente <> ! =
	// no pueden comenzar con
	// numero
	// signos a manenos que sea _
	// no teben llevar espacio
	// Si es una calse simpre inicia con Mayusculas
	// es evitar el codigo espagueti
FinAlgoritmo
