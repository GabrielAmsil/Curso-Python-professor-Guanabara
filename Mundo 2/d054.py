# Desafio 054
# Contar quantas pessoas são maiores de idade

from datetime import date

maior = 0
menor = 0

for i in range(7):
    ano = int(input("Ano de nascimento: "))
    idade = date.today().year - ano

    if idade >= 18:
        maior += 1
    else:
        menor += 1

print("Maiores de idade:", maior)
print("Menores de idade:", menor)