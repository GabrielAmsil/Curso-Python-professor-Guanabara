# Desafio 051
# Progressão Aritmética

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

for i in range(10):
    print(primeiro + i * razao, end=" -> ")
print("FIM")