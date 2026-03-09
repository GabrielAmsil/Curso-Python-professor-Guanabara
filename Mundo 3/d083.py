lista = []
pares = []
impares = []

while True:
    n = int(input("Número: "))
    lista.append(n)

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    resp = input("Continuar? (S/N): ").upper()
    if resp == "N":
        break

print("Lista completa:", lista)
print("Pares:", pares)
print("Ímpares:", impares)