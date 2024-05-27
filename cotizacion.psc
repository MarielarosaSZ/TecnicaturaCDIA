Algoritmo sin_titulo
	Escribir "CASA DE CAMBIO"
	Escribir "ELIJA UNA OPCION"
	Escribir "1 - DOLAR A PESOS"
	eSCRIBIR "2 - PESOS A DOLAR"
	
	Leer OP
	Escribir "INGRESE COTIZACIÓN DOLAR HOY"
	Leer COT
	Si OP = 1 Entonces
		Escribir "INGRESE CANTIDAD DE DOLARES"
		Leer CANT
		PESOS <- CANT * COT
		Escribir "$ ", PESOS
	
	SiNo
		Escribir "INGRESE CANTIDAD DE PESOS"
		Leer CANT
		DOLARES <- CANT / COT
		Escribir "U$D ", DOLARES
	Fin Si
	
FinAlgoritmo
