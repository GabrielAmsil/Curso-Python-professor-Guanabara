# Desafio 044
# Gerenciador de pagamentos

preco = float(input("Preço do produto: "))

print("1 - Dinheiro/cheque")
print("2 - Cartão à vista")
print("3 - Cartão 2x")
print("4 - Cartão 3x ou mais")

opcao = int(input("Escolha a opção: "))

if opcao == 1:
    total = preco * 0.90
elif opcao == 2:
    total = preco * 0.95
elif opcao == 3:
    total = preco
elif opcao == 4:
    total = preco * 1.20
else:
    total = preco

print("Total a pagar:", total)