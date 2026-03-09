import random

jogos = int(input("Quantos jogos gerar? "))

for i in range(jogos):
    jogo = random.sample(range(1, 61), 6)
    jogo.sort()
    print("Jogo:", jogo)