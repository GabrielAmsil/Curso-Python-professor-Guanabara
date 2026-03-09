# Desafio 026
# Leia uma frase e mostre:
# Quantas vezes aparece a letra A
# Em que posição aparece a primeira
# Em que posição aparece a última

frase = input("Digite uma frase: ").lower()

print("Quantidade de 'a':", frase.count("a"))
print("Primeira posição:", frase.find("a") + 1)
print("Última posição:", frase.rfind("a") + 1)