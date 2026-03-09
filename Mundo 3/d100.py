import random

numeros = []

def sorteia():
    for i in range(5):
        numeros.append(random.randint(1,10))
    print("Números:", numeros)

def soma_par():
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print("Soma dos pares:", soma)

sorteia()
soma_par()