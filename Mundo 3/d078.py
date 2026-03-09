lista = []

for i in range(5):
    lista.append(int(input("Número: ")))

print("Maior:", max(lista))
print("Posição:", lista.index(max(lista)))

print("Menor:", min(lista))
print("Posição:", lista.index(min(lista)))