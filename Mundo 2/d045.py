# Desafio 045
# Jogo Jokenpô

import random

print("0 - Pedra")
print("1 - Papel")
print("2 - Tesoura")

jogador = int(input("Escolha: "))
computador = random.randint(0, 2)

if jogador == computador:
    print("Empate")
elif (jogador == 0 and computador == 2) or \
     (jogador == 1 and computador == 0) or \
     (jogador == 2 and computador == 1):
    print("Você ganhou!")
else:
    print("Computador ganhou")