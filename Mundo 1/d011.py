# Desafio 011
# Calcule a área de uma parede e a quantidade de tinta necessária

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

area = largura * altura
tinta = area / 2

print("Área da parede:", area, "m²")
print("Quantidade de tinta necessária:", tinta, "L")