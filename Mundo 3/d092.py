from datetime import date

dados = {}

dados["nome"] = input("Nome: ")
nascimento = int(input("Ano de nascimento: "))
dados["idade"] = date.today().year - nascimento

dados["ctps"] = int(input("Carteira de trabalho (0 se não tem): "))

if dados["ctps"] != 0:
    dados["contratacao"] = int(input("Ano de contratação: "))
    dados["salario"] = float(input("Salário: "))
    dados["aposentadoria"] = dados["idade"] + ((dados["contratacao"] + 35) - date.today().year)

print(dados)