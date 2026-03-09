# Desafio 052
# Verificar se um número é primo

num = int(input("Digite um número: "))
total = 0

for i in range(1, num + 1):
    if num % i == 0:
        total += 1

if total == 2:
    print("É número primo")
else:
    print("Não é primo")