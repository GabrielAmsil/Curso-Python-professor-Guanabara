# Desafio 004
# Leia algo e mostre informações sobre o tipo

algo = input("Digite algo: ")

print("Tipo:", type(algo))
print("É número?", algo.isnumeric())
print("É alfabético?", algo.isalpha())
print("É alfanumérico?", algo.isalnum())
print("Está em maiúsculas?", algo.isupper())
print("Está em minúsculas?", algo.islower())