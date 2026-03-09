# Desafio 070
# Estatística de compras

total = mais1000 = menor = cont = 0
barato = ""

while True:
    produto = input("Nome do produto: ")
    preco = float(input("Preço: "))

    total += preco

    if preco > 1000:
        mais1000 += 1

    if cont == 0 or preco < menor:
        menor = preco
        barato = produto

    cont += 1

    resp = input("Continuar? [S/N] ").upper()
    if resp == "N":
        break

print("Total gasto:", total)
print("Produtos acima de 1000:", mais1000)
print("Produto mais barato:", barato)