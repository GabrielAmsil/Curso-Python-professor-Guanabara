palavras = (
    "python","curso","programador",
    "teclado","monitor"
)

for palavra in palavras:
    print("\nNa palavra", palavra, "tem:", end=" ")
    for letra in palavra:
        if letra in "aeiou":
            print(letra, end=" ")