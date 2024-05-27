"""
Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo)
 no repetidas, guardarlos en una lista y mostrarlos. 

Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarlo

Guardar en un diccionario los datos de una persona: nombre, apellido, dni, email, fecha de nacimiento.

En un nuevo diccionario llamado familia guardar 4 personas, cada una de ellas con los mismos 5 datos
 (nombre, apellido, dni, email, fecha de nacimiento)

Guardar en una tupla los primeros n números pares. El valor de n que lo ingrese el usuario (input). 
Luego mostrar los datos de la tupla.
"""
listaNombre=[]
i=0
for i in range(10):
    nombre=input("Ingrese un nombre: ")
    
    if nombre in  listaNombre:
        i=i-1
        listaNombre.remove(nombre)
        print("Ese nombre ya está en la lista, ingresa otro")
        listaNombre.append(nombre)
    
    else:
        
listaNombre.sort()
print(listaNombre)


