# Desafio 042
# Verificar tipo de triângulo

a = float(input("Primeiro lado: "))
b = float(input("Segundo lado: "))
c = float(input("Terceiro lado: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Triângulo EQUILÁTERO")
    elif a == b or a == c or b == c:
        print("Triângulo ISÓSCELES")
    else:
        print("Triângulo ESCALENO")
else:
    print("Não forma triângulo")