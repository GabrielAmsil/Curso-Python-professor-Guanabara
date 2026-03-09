# Desafio 058
# Jogo de adivinhação com tentativas

import random

numero = random.randint(0, 10)
tentativas = 0

while True:
    palpite = int(input("Tente adivinhar: "))
    tentativas += 1

    if palpite == numero:
        break
    else:
        print("Errado, tente novamente")

print("Você acertou com", tentativas, "tentativas")