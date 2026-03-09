import random
import time

jogo = {}

for i in range(1,5):
    jogo[f"jogador{i}"] = random.randint(1,6)

for k, v in jogo.items():
    print(f"{k} tirou {v}")
    time.sleep(1)

ranking = sorted(jogo.items(), key=lambda x: x[1], reverse=True)

print("\nRanking:")
for i, v in enumerate(ranking):
    print(f"{i+1}º lugar: {v[0]} com {v[1]}")