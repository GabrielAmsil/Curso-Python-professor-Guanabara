valor = int(input("Valor a sacar: R$"))

ced50 = valor // 50
valor %= 50

ced20 = valor // 20
valor %= 20

ced10 = valor // 10
valor %= 10

ced1 = valor

print("50:", ced50)
print("20:", ced20)
print("10:", ced10)
print("1:", ced1)