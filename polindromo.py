palabra = input("Introduce una palabra: ")
reversed_palabra = palabra
palabra = list(palabra)
reversed_palabra = list(reversed_palabra)
reversed_palabra.reverse()
if palabra == reversed_palabra:
    print("Es un palíndromo")
    print(palabra)
    print(reversed_palabra)
else:
    print("No es un palíndromo")
    print(palabra)
    print(reversed_palabra)