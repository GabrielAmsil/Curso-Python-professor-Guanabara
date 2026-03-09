pessoas = []
dados = []
maior = menor = 0

while True:
    dados.append(input("Nome: "))
    dados.append(float(input("Peso: ")))

    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    resp = input("Continuar? (S/N): ").upper()
    if resp == "N":
        break

print("Total de pessoas:", len(pessoas))