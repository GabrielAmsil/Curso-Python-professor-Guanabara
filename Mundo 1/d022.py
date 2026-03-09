# Desafio 022
# Leia o nome completo de uma pessoa e mostre:
# Nome em maiúsculas
# Nome em minúsculas
# Quantas letras tem (sem espaços)
# Quantas letras tem o primeiro nome

nome = input("Digite seu nome completo: ").strip()

print("Maiúsculas:", nome.upper())
print("Minúsculas:", nome.lower())
print("Total de letras:", len(nome.replace(" ", "")))
print("Letras do primeiro nome:", len(nome.split()[0]))