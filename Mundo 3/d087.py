matriz = []
soma_pares = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Valor [{i},{j}]: "))
        linha.append(valor)

        if valor % 2 == 0:
            soma_pares += valor

    matriz.append(linha)

print("Soma dos pares:", soma_pares)