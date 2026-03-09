# Desafio 029
# Radar de velocidade

vel = float(input("Qual é a velocidade do carro? "))

if vel > 80:
    multa = (vel - 80) * 7
    print("Você foi multado!")
    print("Valor da multa:", multa)

print("Dirija com segurança!")