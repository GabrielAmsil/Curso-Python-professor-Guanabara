times = (
    "Palmeiras","Flamengo","Atlético-MG","Grêmio",
    "Botafogo","Bragantino","Fluminense","Athletico",
    "São Paulo","Fortaleza","Cuiabá","Corinthians",
    "Cruzeiro","Vasco","Bahia","Santos",
    "Goiás","Coritiba","América-MG","Internacional"
)

print("Top 5:", times[:5])
print("Últimos 4:", times[-4:])
print("Ordem alfabética:", sorted(times))
print("Posição do Flamengo:", times.index("Flamengo")+1)