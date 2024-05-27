Algoritmo mAYOR_mENOR
	Escribir "INGRESAR TRES NÚMEROS DISTINTOS"
	Leer A,B,C
	Si (A>B) Y (B>C) Entonces
		MA <- A
		ME <- C
	SiNo
		Si (A<B) Y (B<C) Entonces
			MA <- C
			ME <- A
		SiNo
			Si (B<C) Y (C<A) Entonces
				MA <- A
				ME <- B
			SiNo
				Si (B>C) Y (C>A) Entonces
					MA <- B
					ME <- A
				SiNo
					Si (C>A) Y (A>B) Entonces
						MA <- C
						ME <- B
					SiNo
						MA <- B
						ME <- C
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	Fin Si
	Escribir "EL MAYOR ES: ", MA
	Escribir "EL MENOR ES: ", ME
FinAlgoritmo
