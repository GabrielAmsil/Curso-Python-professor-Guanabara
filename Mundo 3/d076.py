produtos = (
    "Lápis",1.75,
    "Borracha",2.00,
    "Caderno",15.90,
    "Estojo",25.00,
    "Mochila",120.00
)

for i in range(0, len(produtos), 2):
    print(produtos[i], "R$", produtos[i+1])