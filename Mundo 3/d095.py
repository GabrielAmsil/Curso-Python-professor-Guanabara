time = []

while True:
    jogador = {}

    jogador["nome"] = input("Nome: ")
    partidas = int(input("Partidas: "))

    gols = []
    for i in range(partidas):
        gols.append(int(input("Gols: ")))

    jogador["gols"] = gols
    jogador["total"] = sum(gols)

    time.append(jogador)

    resp = input("Continuar? ")
    if resp == "N":
        break

print(time)