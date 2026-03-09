# Desafio 059
# Menu de opções

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

opcao = 0

while opcao != 5:
    print("1 - Somar")
    print("2 - Multiplicar")
    print("3 - Maior")
    print("4 - Novos números")
    print("5 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        print("Soma:", n1 + n2)
    elif opcao == 2:
        print("Multiplicação:", n1 * n2)
    elif opcao == 3:
        print("Maior:", max(n1, n2))
    elif opcao == 4:
        n1 = int(input("Novo número: "))
        n2 = int(input("Novo número: "))