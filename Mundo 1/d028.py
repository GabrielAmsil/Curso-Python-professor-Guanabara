# Desafio 028
# Jogo de adivinhação

import random

numero = random.randint(0, 5)

palpite = int(input("Tente adivinhar o número entre 0 e 5: "))

if palpite == numero:
    print("Você acertou!")
else:
    print("Você errou! O número era", numero)