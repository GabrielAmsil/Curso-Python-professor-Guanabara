numeros = []

while True:
    n = int(input("Digite um número: "))
    numeros.append(n)

    resp = input("Continuar? (S/N): ").upper()
    if resp == "N":
        break

print("Quantidade de números:", len(numeros))

numeros.sort(reverse=True)
print("Lista decrescente:", numeros)

if 5 in numeros:
    print("O número 5 está na lista")
else:
    print("O número 5 não está na lista")