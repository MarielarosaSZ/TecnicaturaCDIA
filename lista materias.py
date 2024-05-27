fin= "n"
materias=[]
# notas=[]
while fin != "s":
    materias.append(input("Ingrese una materia : "))
    notas=float(input("Ingrese la nota correspondiente : "))
    if notas < 6 :
        materias.remove()
    fin=input("¿Fué la última? (s / n) : ")
print ("Debes repetir las siguientes materias:  ")
for i in range(len(materias)):
    print ( materias[i])
            
