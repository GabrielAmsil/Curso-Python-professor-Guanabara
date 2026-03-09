# Desafio 065
# Média de números digitados

resp = "S"
soma = cont = 0
maior = menor = 0

while resp == "S":
    num = int(input("Digite um número: "))
    soma += num
    cont += 1

    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = input("Quer continuar? [S/N] ").upper()

media = soma / cont

print("Média:", media)
print("Maior:", maior)
print("Menor:", menor)