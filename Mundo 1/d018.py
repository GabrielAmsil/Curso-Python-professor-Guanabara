# Desafio 018
# Mostrar seno, cosseno e tangente

import math

angulo = float(input("Digite o ângulo: "))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print("Seno:", seno)
print("Cosseno:", cosseno)
print("Tangente:", tangente)