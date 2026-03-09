# Desafio 031
# Calcule o preço de uma viagem
# Até 200km → R$0.50 por km
# Acima de 200km → R$0.45 por km

distancia = float(input("Qual é a distância da viagem em km? "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print("O preço da passagem é R$", preco)