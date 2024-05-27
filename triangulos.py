n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(1, i+1, 2):
        print(j, end=" ")
    print("")