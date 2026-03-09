# Desafio 041
# Classificação de atletas por idade

from datetime import date

ano = int(input("Ano de nascimento: "))
idade = date.today().year - ano

if idade <= 9:
    print("Categoria: MIRIM")
elif idade <= 14:
    print("Categoria: INFANTIL")
elif idade <= 19:
    print("Categoria: JUNIOR")
elif idade <= 20:
    print("Categoria: SÊNIOR")
else:
    print("Categoria: MASTER")