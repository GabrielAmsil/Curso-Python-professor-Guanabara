numeros = []

while True:
    n = int(input("Número: "))

    if n not in numeros:
        numeros.append(n)

    resp = input("Continuar? (S/N): ").upper()

    if resp == "N":
        break

numeros.sort()
print(numeros)