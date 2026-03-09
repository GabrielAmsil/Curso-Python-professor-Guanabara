# Desafio 034
# Aumento salarial
# Salários maiores que 1250 → aumento de 10%
# Menores ou iguais → aumento de 15%

salario = float(input("Digite o salário: "))

if salario > 1250:
    novo = salario * 1.10
else:
    novo = salario * 1.15

print("Novo salário:", novo)