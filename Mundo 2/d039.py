# Desafio 039
# Alistamento militar

from datetime import date

ano = int(input("Ano de nascimento: "))

atual = date.today().year
idade = atual - ano

if idade < 18:
    print("Ainda vai se alistar")
elif idade == 18:
    print("Hora de se alistar")
else:
    print("Já passou do tempo de alistamento")