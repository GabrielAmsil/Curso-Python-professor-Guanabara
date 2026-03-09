# Desafio 040
# Calcular média e mostrar situação do aluno

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))

media = (n1 + n2) / 2

if media < 5:
    print("Reprovado")
elif 5 <= media < 7:
    print("Recuperação")
else:
    print("Aprovado")