frase=input("Ingrese una frase : ")
letra=input("cuál letra quiere contar? : " )
fin=len(frase)
CANT = 0
for i in frase:
    if letra == i:
        CANT +=  1
print( "La frase tiene " , CANT , "letras ", letra )