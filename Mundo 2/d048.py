# Desafio 048
# Soma de todos os números ímpares múltiplos de 3 entre 1 e 500

soma = 0
contador = 0

for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        soma += i
        contador += 1

print("Quantidade:", contador)
print("Soma:", soma)