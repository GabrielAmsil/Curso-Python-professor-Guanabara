jogador = {}

jogador["nome"] = input("Nome do jogador: ")
partidas = int(input("Quantas partidas jogou? "))

gols = []

for i in range(partidas):
    gols.append(int(input(f"Gols na partida {i}: ")))

jogador["gols"] = gols
jogador["total"] = sum(gols)

print(jogador)