# Desafio 069
# Cadastro de pessoas

maior18 = homens = mulheres20 = 0

while True:
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").upper()

    if idade >= 18:
        maior18 += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres20 += 1

    resp = input("Quer continuar? [S/N] ").upper()
    if resp == "N":
        break

print("Maiores de 18:", maior18)
print("Homens cadastrados:", homens)
print("Mulheres com menos de 20:", mulheres20)