# Desafio 067
# Tabuada com parada

while True:
    n = int(input("Quer ver a tabuada de qual valor? "))
    if n < 0:
        break

    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

print("Programa encerrado")