Algoritmo Mayor_menor
	Escribir "escribe tres números distintos"
	Leer A, B, C
	Si (A>B)  Entonces
		Si (A>C) Entonces
			MA <- A
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
