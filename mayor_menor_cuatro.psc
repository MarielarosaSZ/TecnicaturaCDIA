Algoritmo mayor_menor_cuatro
	Escribir "introduce 4 numeros distintos"
	Leer A, B, C, D
	Si (A>B)  Entonces
		Si (A>C) Entonces
			Si (A>D) Entonces
				MA <- A
				Si (B>C)  Entonces
					Si (C>D) Entonces
						ME <- D
						
					SiNo
						ME <- C
					Fin Si
				SiNo
					Si (B>D) Entonces
						ME <- D
					SiNo
						ME <- B
					Fin Si
				Fin Si
			SiNo
				MA <- D
				
			Fin Si
			
			Si (B>C) Entonces
				ME <- C
			SiNo
				ME <- B
			Fin Si
		SiNo
			MA <-C
			ME <- B
		Fin Si
	SiNo
		Si (B>C) Entonces
			MA <- B
			Si (A>C) Entonces
				ME <- C
			SiNo
				ME <- A
			Fin Si
		SiNo
			MA <- C
			ME <- A
		Fin Si
	Fin Si
	Escribir " EL MAYOR ES: ", MA
	Escribir "EL MENOR ES: ", ME
FinAlgoritmo
