# Desafio 068
# Jogo par ou ímpar

import random

vitorias = 0

while True:
    jogador = int(input("Digite um valor: "))
    escolha = input("Par ou Ímpar? ").upper()

    computador = random.randint(0, 10)
    total = jogador + computador

    if total % 2 == 0:
        resultado = "PAR"
    else:
        resultado = "ÍMPAR"

    print("Você:", jogador, "Computador:", computador)

    if escolha == resultado:
        print("Você ganhou!")
        vitorias += 1
    else:
        print("Você perdeu!")
        break

print("Vitórias consecutivas:", vitorias)