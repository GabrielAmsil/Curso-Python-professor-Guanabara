matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Valor [{i},{j}]: ")))
    matriz.append(linha)

for linha in matriz:
    print(linha)