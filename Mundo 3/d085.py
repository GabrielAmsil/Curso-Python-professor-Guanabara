numeros = [[], []]

for i in range(7):
    n = int(input("Número: "))

    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)

print("Pares:", sorted(numeros[0]))
print("Ímpares:", sorted(numeros[1]))