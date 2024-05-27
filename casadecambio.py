print ("CASA DE CAMBIO")
print ("ELIJA UNA OPCIÓN")
print ("1-DÓLARES A PESOS")
print ("2-PESOS A DÓLARES")
OP = input ("OPCIÓN:  ")
COT = float(input ("INGRESE COTIZACIÓN DEL DOLAR HOY  "))
if OP == "1" :
    CANT = float(input ("INGRESE CANTIDAD DE DÓLARES U$D "))
    PESOS = CANT * COT
    print ("$ ", CANT, "  EQUIVALEN A $ ", PESOS)
else:
    CANT = float(input ("INGRESE CANTIDAD DE PESOS $ "))
    DOLARES = CANT / COT
    print ("$ ", CANT, "  EQUIVALEN A U$D ", DOLARES)