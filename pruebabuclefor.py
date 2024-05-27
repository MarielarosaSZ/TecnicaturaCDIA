#n = int(input("Introduce un número entero positivo: "))
#for i in range(n, -1, -1):
#    print(i, end=", ")

#n = int(input("Introduce la altura del triángulo (entero positivo): "))
#for i in range(n):
#    for j in range(i+1):
#        print("$" end="")
#    print("")

#n = int(input("haremos la tabla del : "))
#for i in range(1, 10):
#    N= n*i
#    print(n , "x" , i , "=" , N , end="")
#   print()

n = int(input("Introduce la altura del triángulo (entero positivo): "))
impar=-1
for i in range(n):
    for j in range(i+1):
        impar = impar+2
        print( impar , " ", end="")
    impar=-1
    print("")