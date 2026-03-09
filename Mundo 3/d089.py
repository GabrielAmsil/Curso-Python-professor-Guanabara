boletim = []

while True:
    nome = input("Nome: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))

    media = (n1 + n2) / 2
    boletim.append([nome, [n1, n2], media])

    resp = input("Continuar? (S/N): ").upper()
    if resp == "N":
        break

for aluno in boletim:
    print(aluno[0], "média:", aluno[2])