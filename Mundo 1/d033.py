# Desafio 033
# Leia três números e mostre o maior e o menor

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

print("Maior:", maior)
print("Menor:", menor)