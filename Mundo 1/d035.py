# Desafio 035
# Verifique se três segmentos podem formar um triângulo

a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

if a + b > c and a + c > b and b + c > a:
    print("Pode formar um triângulo")
else:
    print("Não pode formar um triângulo")