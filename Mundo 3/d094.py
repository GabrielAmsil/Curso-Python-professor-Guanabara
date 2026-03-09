pessoas = []
soma = 0

while True:
    pessoa = {}

    pessoa["nome"] = input("Nome: ")
    pessoa["sexo"] = input("Sexo (M/F): ")
    pessoa["idade"] = int(input("Idade: "))

    soma += pessoa["idade"]
    pessoas.append(pessoa)

    resp = input("Continuar? (S/N): ")
    if resp == "N":
        break

media = soma / len(pessoas)

print("Média de idade:", media)