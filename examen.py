"""
dias = ( "Lunes", "Martes", "Miercoles", "Jueves")

dias.append("Viernes")

print(dias)
"""
"""
unidadesDeLeche = int(input("Ingrese la cantidad de unidades de leche que compra el cliente"))
esJubiado = int(input("Ingrese 0 si el cliente no es jubilado, cualquier otro numero si el cliente es Jubilado"))

montoParcial = unidadesDeLeche * 1000
print(f"unidadesDeLeche {unidadesDeLeche} esJubiado {esJubiado}")

if(unidadesDeLeche <=12 and not esJubiado):
    print("unidadesDeLeche <=12 and not esJubiado")
    montoAPagar = montoParcial
elif((unidadesDeLeche >12 and unidadesDeLeche <= 24) and not esJubiado):
    print("(unidadesDeLeche >12 and unidadesDeLeche <= 24) and not esJubiado")
    montoAPagar = montoParcial * 0.9
elif(unidadesDeLeche > 24 and not esJubiado):
    print("unidadesDeLeche > 24 and not esJubiado")
    montoAPagar = montoParcial * 0.85
if(unidadesDeLeche <=12 and esJubiado):
    print("unidadesDeLeche <=12 and esJubiado")
    montoAPagar = montoParcial * 0.9
elif((unidadesDeLeche >12 and unidadesDeLeche <= 24) and esJubiado):
    print("(unidadesDeLeche >12 and unidadesDeLeche <= 24) and esJubiado")
    montoAPagar = montoParcial * 0.8
elif(unidadesDeLeche > 24 and esJubiado):
    print("unidadesDeLeche > 24 and esJubiado")
    montoAPagar = montoParcial * 0.75

print(f"El monto sin descuento es: {montoParcial} y el monto total a pagar es: {montoAPagar}")
"""

""" def find_duplicates(elements):
    duplicates, seen = set(), set()
    for element in elements:
        if element in seen:
            duplicates.add(element)
        seen.add(element)
    return list(duplicates)
print(find_duplicates())
"""

def find_pairs(l, x):
    pairs = []
    for (i, el_1) in enumerate(l):
        for (j, el_2) in enumerate(l[i+1:]):
            if el_1 + el_2 == x:
                pairs.append((el_1, el_2))
    return pairs

print( find_pairs(3,8))


