# Desafio 036
# Aprovando empréstimo

valor_casa = float(input("Valor da casa: "))
salario = float(input("Salário do comprador: "))
anos = int(input("Quantos anos para pagar? "))

prestacao = valor_casa / (anos * 12)

if prestacao > salario * 0.30:
    print("Empréstimo negado")
else:
    print("Empréstimo aprovado")