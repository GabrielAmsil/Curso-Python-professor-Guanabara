# Desafio 015
# Calcular preço de aluguel de carro

dias = int(input("Quantos dias alugado? "))
km = float(input("Quantos km rodados? "))

preco = (dias * 60) + (km * 0.15)

print("O total a pagar é:", preco)