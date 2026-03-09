# Desafio 050
# Soma de números pares

soma = 0

for i in range(6):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        soma += n

print("Soma dos pares:", soma)