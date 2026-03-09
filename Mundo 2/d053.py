# Desafio 053
# Verificar se uma frase é palíndromo

frase = input("Digite uma frase: ").replace(" ", "").lower()

if frase == frase[::-1]:
    print("É palíndromo")
else:
    print("Não é palíndromo")