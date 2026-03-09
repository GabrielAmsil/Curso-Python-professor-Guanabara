valores = (
    int(input("Número: ")),
    int(input("Número: ")),
    int(input("Número: ")),
    int(input("Número: "))
)

print("Quantidade de 9:", valores.count(9))

if 3 in valores:
    print("Posição do 3:", valores.index(3)+1)

print("Pares:")
for v in valores:
    if v % 2 == 0:
        print(v)