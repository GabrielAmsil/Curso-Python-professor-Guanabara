# Desafio 056
# Analisar dados de um grupo

soma_idade = 0
media = 0
mais_velho = ""
idade_velho = 0
mulheres = 0

for i in range(4):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()

    soma_idade += idade

    if sexo == "M" and idade > idade_velho:
        idade_velho = idade
        mais_velho = nome

    if sexo == "F" and idade < 20:
        mulheres += 1

media = soma_idade / 4

print("Média de idade:", media)
print("Homem mais velho:", mais_velho)
print("Mulheres com menos de 20:", mulheres)