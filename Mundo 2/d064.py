# Desafio 064
# Soma de números até digitar 999

soma = 0
cont = 0

num = int(input("Digite um número (999 para parar): "))

while num != 999:
    soma += num
    cont += 1
    num = int(input("Digite um número (999 para parar): "))

print("Quantidade:", cont)
print("Soma:", soma)