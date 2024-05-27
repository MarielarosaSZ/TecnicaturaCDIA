"""
En una escuela, luego de tomar un determinado examen, es necesario calcular el promedio de notas (las notas van de 0 a 10)
 de los alumnos de un curso. Se necesita saber si el rendimiento ha sido elevado (el promedio es mayor a 8), 
 aceptable (el promedio está comprendido entre 6 y 8) o bajo (promedio es inferior a 6). 
  Para tener en cuenta: las autoridades del colegio saben cuántos estudiantes del curso han rendido el examen.
"""

cantidad=int(input ("Cantidad de Alumnos que Rindieron: "))
suma=0
for i in range(cantidad):
    nota=int(input("Ingrese nota :"))
    suma=suma+nota

promedio=suma/cantidad
if promedio > 8:
    print ("El rendimiento ha sido ELEVADO")
if promedio < 6:
    print("El rendimiento ha sido BAJO")
else :
    print("El rendimiento ha sido ACEPTABLE")

