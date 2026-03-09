# Desafio 057
# Validação de sexo

sexo = input("Digite seu sexo (M/F): ").upper()

while sexo not in "MF":
    sexo = input("Valor inválido. Digite M ou F: ").upper()

print("Sexo registrado:", sexo)