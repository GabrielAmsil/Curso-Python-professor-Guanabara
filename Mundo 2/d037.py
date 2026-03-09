# Desafio 037
# Converter número para binário, octal ou hexadecimal

numero = int(input("Digite um número inteiro: "))

print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    print(bin(numero)[2:])
elif opcao == 2:
    print(oct(numero)[2:])
elif opcao == 3:
    print(hex(numero)[2:])
else:
    print("Opção inválida")