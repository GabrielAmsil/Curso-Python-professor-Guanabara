# Desafio 024
# Verifique se a cidade começa com "Santo"

cidade = input("Digite o nome da cidade: ").strip()

print(cidade[:5].lower() == "santo")