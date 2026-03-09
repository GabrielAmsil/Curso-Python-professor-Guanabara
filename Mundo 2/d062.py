# Desafio 062
# PA com opção de mostrar mais termos

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

termo = primeiro
cont = 1
total = 10
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end=" → ")
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos a mais? "))

print("Progressão finalizada")