# Desafio 055
# Mostrar maior e menor peso

maior = 0
menor = 0

for i in range(5):
    peso = float(input("Peso: "))

    if i == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print("Maior peso:", maior)
print("Menor peso:", menor)