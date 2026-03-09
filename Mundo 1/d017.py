# Desafio 017
# Calcular a hipotenusa de um triângulo

import math

co = float(input("Cateto oposto: "))
ca = float(input("Cateto adjacente: "))

h = math.hypot(co, ca)

print("A hipotenusa é:", h)